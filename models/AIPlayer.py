import os
import neat
import pickle
from models.BasePlayer import BasePlayer


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
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'neat_config.txt')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    with open('best.pickle', 'rb') as file:
      winner = pickle.load(file)
    self.neural_network = neat.nn.FeedForwardNetwork.create(winner, config)
