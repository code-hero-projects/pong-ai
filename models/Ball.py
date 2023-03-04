class Ball:
  def __init__(self, x, y, width):
    self.x = x
    self.y = y
    self.width = width
  
  def move(self, velocity):
    self.x += velocity
    self.y += velocity