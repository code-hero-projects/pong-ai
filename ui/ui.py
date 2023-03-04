import pygame

from ui.consts import COLOR_BLACK, WINDOW_HEIGHT, WINDOW_WIDTH, MIDDLE_LINE_SPACING
from assets.assets import get_player, get_middle_line

class UI:
  def __init__(self, game):
    self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    self.game = game
  
  def draw_window(self):
    self.window.fill(COLOR_BLACK)

    self._draw_middle_line()
    self._draw_players()

    pygame.display.update()

  def _draw_players(self):
    self._draw_player(self.game.player_one)
    self._draw_player(self.game.player_two)

  def _draw_player(self, player):
    player_image = get_player().image
    self.window.blit(player_image, (player.location.x, player.location.y))

  def _draw_middle_line(self):
    middle_line_image = get_middle_line()
    
    x = WINDOW_WIDTH / 2 - middle_line_image.width / 2
    for middle_line_counter in range(10):
      y = (middle_line_counter * (middle_line_image.height * 2 + MIDDLE_LINE_SPACING)) + MIDDLE_LINE_SPACING
      self.window.blit(middle_line_image.image, (x, y))

  def _draw_ball(self):
    pass

  def _draw_score(self):
    pass