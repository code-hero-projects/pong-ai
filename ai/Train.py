import neat
import pickle
from ai.TrainStorage import TrainStorage
from ai.TrainUI import TrainUI
from ai.consts import BEST_GENOME_FILENAME, GENERATIONS, MAX_HITS, NEAT_CONFIG_FILENAME, SCORE_MULTIPLIER
from consts import WINDOW_WIDTH
from controller.consts import FPS
from controller.game import Game


class Train(Game):
  def __init__(self, ball, player_one):
    super().__init__(player_one, None, ball)
    self.ui = TrainUI(self, player_one == None)
    self.player_one_round_score = 0
    self.player_two_round_score = 0
    self.generation = 1

  def neat(self, generation=None):
    self.train_storage = TrainStorage(generation)

    population = self._setup_population(generation)

    winner = population.run(self._evaluate_genomes, GENERATIONS)

    with open(BEST_GENOME_FILENAME, "wb") as f:
      pickle.dump(winner, f)

  def _setup_population(self, generation):
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

    return population

  def _evaluate_genomes(self, genomes, config):
    pass

  def _update_score(self):
    if self.ball.x < 0:
      self.player_two.score += 1
      self.player_two_round_score += 1

    elif self.ball.x > WINDOW_WIDTH:
      self.player_one.score += 1
      self.player_one_round_score += 1

  def _reset_round(self):
    self.ball.reset()
    self.player_one_round_score = 0
    self.player_two_round_score = 0
    self.player_one.reset()
    self.player_two.reset()