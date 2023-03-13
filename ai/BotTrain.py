import pygame
import time
import neat
from ai.AIPlayer import AIPlayer
from ai.consts import MAX_HITS, SCORE_MULTIPLIER
from controller.consts import FPS
from ai.Train import Train
from consts import PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN, WINDOW_HEIGHT, WINDOW_WIDTH

class BotTrain(Train):
  def __init__(self, ball, player_one):
    super().__init__(ball, player_one)

  def _evaluate_genomes(self, genomes, config):
    pass
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