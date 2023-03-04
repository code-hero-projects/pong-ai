import pygame
from consts import WINDOW_HEIGHT


class HumanPlayer:
  def __init__(self, name, score, x, y, velocity, width, height, key_up, key_down):
    self.name = name
    self.score = score
    self.x = self.original_x = x
    self.y = self.original_y = y
    self.velocity = velocity
    self.width = width
    self.height = height
    self.key_up = key_up
    self.key_down = key_down
  
  def move(self):
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[self.key_up]:
      self._move_up()
    elif keys_pressed[self.key_down]:
      self._move_down()

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