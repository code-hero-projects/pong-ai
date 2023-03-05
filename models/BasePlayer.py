from consts import WINDOW_HEIGHT


class BasePlayer:
  def __init__(self, name, score, x, y, velocity, width, height):
    self.name = name
    self.score = score
    self.x = self.original_x = x
    self.y = self.original_y = y
    self.velocity = velocity
    self.width = width
    self.height = height

  def move(self):
    pass

  def reset(self):
    self.x = self.original_x
    self.y = self.original_y
  
  def _move_up(self):
    new_y = self.y - self.velocity

    if new_y > 0:
      self.y = new_y

  def _move_down(self):
    new_y = self.y + self.velocity

    if new_y + self.height < WINDOW_HEIGHT:
      self.y = new_y