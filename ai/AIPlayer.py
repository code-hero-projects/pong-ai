from consts import WINDOW_HEIGHT


class AIPlayer:
    def __init__(self, name, score, x, y, velocity, width, height, ball, neural_network, genome):
      self.name = name
      self.score = score
      self.x = self.original_x = x
      self.y = self.original_y = y
      self.velocity = velocity
      self.width = width
      self.height = height
      self.ball = ball
      self.neural_network = neural_network
      self.genome = genome
      self.hits = 0

    def reset(self):
      self.x = self.original_x
      self.y = self.original_y
    
    def move(self):
      output = self.neural_network.activate((self.y, abs(self.x - self.ball.x), self.ball.y))
      decision = output.index(max(output))

      # valid = True
      if decision == 0:
        valid = False
      elif decision == 1:
        valid = self._move_up()
      else:
        valid = self._move_down()

      if not valid:
        self.genome.fitness -= 0.01

    def _move_up(self):
      new_y = self.y - self.velocity

      if new_y > 0:
        self.y = new_y
        return True
      else:
        return False
      

    def _move_down(self):
      new_y = self.y + self.velocity

      if new_y + self.height < WINDOW_HEIGHT:
        self.y = new_y
        return True
      else:
        return False