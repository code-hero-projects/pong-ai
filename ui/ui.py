import pygame

from ui.consts import COLOR_BLACK, WINDOW_HEIGHT, WINDOW_WIDTH
from assets.assets import get_player

class UI:
  def __init__(self, game):
    self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    self.game = game
  
  def draw_window(self):
    self.window.fill(COLOR_BLACK)

    self._draw_players()

    pygame.display.update()

  def _draw_players(self):
    self._draw_player(self.game.player_one)
    self._draw_player(self.game.player_two)

  def _draw_player(self, player):
    player_image = get_player()
    player_location = (player.location.x, player.location.y)
    self.window.blit(player_image, player_location)

  def _draw_ball(self):
    pass

  def _draw_score(self):
    pass