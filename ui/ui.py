import pygame

from ui.consts import COLOR_BLACK

class UI:
  def __init__(self, game):
    self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.game = game
  
  def draw_window(self):
    self.window.fill(COLOR_BLACK)
    pygame.display.update()

  def _draw_players(self):
    pass

  def _draw_ball(self):
    pass

  def _draw_score(self):
    pass