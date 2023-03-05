import pygame
from models.BasePlayer import BasePlayer


class HumanPlayer(BasePlayer):
  def __init__(self, name, score, x, y, velocity, width, height, key_up, key_down):
    super().__init__(name, score, x, y, velocity, width, height)
    self.key_up = key_up
    self.key_down = key_down
  
  def move(self):
    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[self.key_up]:
      super()._move_up()
    elif keys_pressed[self.key_down]:
      super()._move_down()