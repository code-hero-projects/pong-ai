from consts import WINDOW_HEIGHT


class Player:
  def __init__(self, name, score, x, y, width, height):
    self.name = name
    self.score = score
    self.x = x
    self.y = y
    self.width = width
    self.height = height
  
  def move_up(self, velocity):
    new_y = self.y - velocity

    if new_y > 0:
      self.y = new_y

  def move_down(self, velocity):
    new_y = self.y + velocity

    if new_y + self.height < WINDOW_HEIGHT:
      self.y = new_y