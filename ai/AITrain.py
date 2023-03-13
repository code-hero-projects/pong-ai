import pygame
import time
import neat
from ai.AIPlayer import AIPlayer
from ai.consts import MAX_HITS
from controller.consts import FPS
from ai.Train import Train
from consts import PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN, WINDOW_HEIGHT, WINDOW_WIDTH

class AITrain(Train):
  def __init__(self, ball):
    super().__init__(ball, None)

  def _evaluate_genomes(self, genomes, config):
    for i, (genome_id1, genome_1) in enumerate(genomes):
      genome_1.fitness = 0
      for genome_id2, genome_2 in genomes[min(i+1, len(genomes) - 1):]:
        if genome_2.fitness == None:
          genome_2.fitness = 0
        self._train_ai(genome_id1, genome_1, genome_id2, genome_2, config)
      
    self.generation += 1

  def _train_ai(self, genome_id1, genome_1, genome_id2, genome_2, config):
    clock = pygame.time.Clock()
    run = True
    
    start_time = time.time()

    neural_network_1 = neat.nn.FeedForwardNetwork.create(genome_1, config)
    neural_network_2 = neat.nn.FeedForwardNetwork.create(genome_2, config)

    self.player_one = self._create_ai_player_one(genome_1, neural_network_1)
    self.player_two = self._create_ai_player_two(genome_2, neural_network_2)
    
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

        self._calculate_fitness(self.player_one, genome_1, duration)
        self._calculate_fitness(self.player_two, genome_2, duration)

        self._reset_round()
        break

  def _create_ai_player_one(self, genome, neural_network):
    x = SCREEN_EDGE_MARGIN
    y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

    return self._create_ai_player(x, y, genome, neural_network)

  def _create_ai_player_two(self, genome, neural_network):
    x = WINDOW_WIDTH - SCREEN_EDGE_MARGIN - PLAYER_WIDTH
    y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

    return self._create_ai_player(x, y, genome, neural_network)

  def _create_ai_player(self, x, y, genome, neural_network):
    player_name = f'Gen {self.generation}, #{genome.key}'

    return AIPlayer(player_name, 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, self.ball, neural_network, genome)

  def _calculate_fitness(self, player, genome, duration):
    genome.fitness += player.hits + duration