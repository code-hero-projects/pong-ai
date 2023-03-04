import pygame

from ui.consts import BALL_WIDTH, COLOR_BLACK, FONT_MARGIN_TOP, WINDOW_HEIGHT, WINDOW_WIDTH, MIDDLE_LINE_SPACING, FONT, COLOR_WHITE
from assets.assets import get_player, get_middle_line

class UI:
  def __init__(self, game):
    self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    self.game = game
  
  def draw_window(self):
    self.window.fill(COLOR_BLACK)

    self._draw_middle_line()
    self._draw_score()
    self._draw_players()
    self._draw_ball()

    pygame.display.update()

  def _draw_middle_line(self):
    middle_line_image = get_middle_line()
    
    x = WINDOW_WIDTH / 2 - middle_line_image.width / 2
    for middle_line_counter in range(10):
      y = (middle_line_counter * (middle_line_image.height * 2 + MIDDLE_LINE_SPACING)) + MIDDLE_LINE_SPACING
      self.window.blit(middle_line_image.image, (x, y))

  def _draw_score(self):
    score_font = pygame.font.SysFont(FONT, 100)

    score = score_font.render(str(self.game.player_one.score), 1, COLOR_WHITE)
    self.window.blit(score, (WINDOW_WIDTH / 2 - score.get_width() * 2, FONT_MARGIN_TOP))

    score = score_font.render(str(self.game.player_two.score), 1, COLOR_WHITE)
    self.window.blit(score, (WINDOW_WIDTH / 2 + score.get_width(), FONT_MARGIN_TOP))

  def _draw_players(self):
    self._draw_player(self.game.player_one)
    self._draw_player(self.game.player_two)

  def _draw_player(self, player):
    player_image = get_player().image
    self.window.blit(player_image, (player.location))

  def _draw_ball(self):
    ball = self.game.ball
    pygame.draw.circle(self.window, COLOR_WHITE, ball.location, BALL_WIDTH)