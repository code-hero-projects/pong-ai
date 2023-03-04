class Player:
  def __init__(self, name, score, location):
    self.name = name
    self.score = score
    self.location = location
  
  def move_up(self, velocity):
    new_y = self.location[1] - velocity
    self.location = (self.location[0], new_y)

  def move_down(self, velocity):
    new_y = self.location[1] + velocity
    self.location = (self.location[0], new_y)