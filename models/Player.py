from ui.consts import WINDOW_HEIGHT


class Player:
  def __init__(self, name, score, location, body):
    self.name = name
    self.score = score
    self.location = location
    self.body = body
  
  def move_up(self, velocity):
    new_y = self.location[1] - velocity

    if new_y > 0:
      self.location = (self.location[0], new_y)

  def move_down(self, velocity):
    new_y = self.location[1] + velocity

    if new_y + self.body.height < WINDOW_HEIGHT:
      self.location = (self.location[0], new_y)