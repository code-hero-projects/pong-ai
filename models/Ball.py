import random

from consts import RANDOM_BALL_MARGIN, WINDOW_HEIGHT


class Ball:
  def __init__(self, x, y, radius, max_velocity):
    self.x = self.original_x = x
    self.y = self.original_y = y
    self.radius = radius
    self.x_velocity = max_velocity
    self.y_velocity = 0
  
  def move(self):
    self.x += self.x_velocity
    self.y += self.y_velocity
  
  def reset(self):
    self.x = self.original_x
    self.y = self.original_y
    self.y_velocity = 0
    self.x_velocity *= -1
  
  def random(self):
    random_direction = random.randint(1, 100)
    if random_direction > 50:
      self.x_velocity *= -1
    
    random_y = random.randint(RANDOM_BALL_MARGIN, WINDOW_HEIGHT - RANDOM_BALL_MARGIN)
    self.y = random_y

    