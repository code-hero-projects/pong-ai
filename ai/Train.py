import time
import neat
import pygame
import pickle
from ai.AIPlayer import AIPlayer
from ai.TrainStorage import TrainStorage
from ai.consts import BEST_GENOME_FILENAME, GENERATIONS, MAX_HITS, NEAT_CONFIG_FILENAME, SCORE_MULTIPLIER
from consts import PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN, WINDOW_HEIGHT, WINDOW_WIDTH
from controller.consts import FPS
from controller.game import Game
from ui.ui import UI


class Train(Game):
  def __init__(self, player_one, ball):
    super().__init__(player_one, None, ball)
    self.ui = UI(self, True)
    self.player_one_round_score = 0
    self.player_two_round_score = 0
    self.generation = 1

  def neat(self, generation=None):
    self.train_storage = TrainStorage(generation)
    if not generation:
      config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, NEAT_CONFIG_FILENAME)
      population = neat.Population(config)
    else:
      checkpoint = f'neat-checkpoint-{generation}'
      population = neat.Checkpointer.restore_checkpoint(checkpoint)
      self.generation = generation

    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    population.add_reporter(neat.Checkpointer(1))

    winner = population.run(self._evaluate_genomes, GENERATIONS)

    with open(BEST_GENOME_FILENAME, "wb") as f:
      pickle.dump(winner, f)

  def _evaluate_genomes(self, genomes, config):
    for i, (genome_id, genome) in enumerate(genomes):
      if genome.fitness == None:
        genome.fitness = 0
      self._train_ai(genome_id, genome, config)
    
    self._reset_generation()
    self.train_storage.end_generation()
    self.generation += 1

  def _train_ai(self, genome_id, genome, config):
    clock = pygame.time.Clock()
    run = True
    
    start_time = time.time()
    neural_network = neat.nn.FeedForwardNetwork.create(genome, config)
    self.player_two = self._create_ai_player(genome, neural_network)
    self.ball.random()

    while run:
      clock.tick(FPS)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False

      self._play_turn()
      self.ui.draw_window()

      if self.player_one_round_score == 1 or self.player_two_round_score == 1 or self.player_two.hits == MAX_HITS:
        duration = time.time() - start_time
        self._calculate_fitness(genome, duration)
        self.train_storage.add_genome_info(self.generation, genome_id, genome.fitness, self.player_two.hits, self.player_two_round_score)
        self._reset_round()
        break

  def _create_ai_player(self, genome, neural_network):
    x = WINDOW_WIDTH - SCREEN_EDGE_MARGIN - PLAYER_WIDTH
    y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

    player_name = f'Gen {self.generation}, #{genome.key}'

    return AIPlayer(player_name, 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, self.ball, neural_network, genome)

  def _update_score(self):
    if self.ball.x < 0:
      self.player_two.score += 1
      self.player_two_round_score += 1

    elif self.ball.x > WINDOW_WIDTH:
      self.player_one.score += 1
      self.player_one_round_score += 1
  
  def _calculate_fitness(self, genome, duration):
    genome.fitness += self.player_two.hits + self.player_two_round_score * SCORE_MULTIPLIER + duration

  def _reset_round(self):
    self.ball.reset()
    self.player_one_round_score = 0
    self.player_two_round_score = 0
    self.player_one.reset()
    self.player_two.reset()

  def _reset_generation(self):
    self.player_one.score = 0