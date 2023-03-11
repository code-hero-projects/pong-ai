import os
import neat
import pickle
from ai.consts import BEST_GENOME_FILENAME, NEAT_CONFIG_FILENAME
from models.players.BasePlayer import BasePlayer


class AIPlayer(BasePlayer):
  def __init__(self, name, score, x, y, velocity, width, height, ball):
    super().__init__(name, score, x, y, velocity, width, height)
    self.ball = ball
    self._init_neural_network()
  
  def move(self):
    output = self.neural_network.activate((self.y, abs(self.x - self.ball.x), self.ball.y))
    decision = output.index(max(output))

    if decision == 1:
      super()._move_up()
    elif decision == 2:
      super()._move_down()
    
  def _init_neural_network(self):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, NEAT_CONFIG_FILENAME)

    with open(BEST_GENOME_FILENAME, 'rb') as file:
      winner = pickle.load(file)
    self.neural_network = neat.nn.FeedForwardNetwork.create(winner, config)
