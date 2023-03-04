class Ball:
  def __init__(self, x, y, radius, max_velocity):
    self.x = self._original_x = x
    self.y = self._original_y = y
    self.radius = radius
    self.x_velocity = max_velocity
    self.y_velocity = 0
  
  def move(self):
    self.x += self.x_velocity
    self.y += self.y_velocity