import pygame

from ui.consts import COLOR_BLACK, COLOR_LIGHT_GREY, COLOR_ORANGE, FONT_MARGIN_TOP, MIDDLE_LINE_HEIGHT, MIDDLE_LINE_SPACING, FONT, COLOR_WHITE, MIDDLE_LINE_WIDTH
from consts import WINDOW_HEIGHT, WINDOW_WIDTH

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
    x = WINDOW_WIDTH / 2 - MIDDLE_LINE_WIDTH / 2
    for middle_line_counter in range(10):
      y = (middle_line_counter * (MIDDLE_LINE_HEIGHT * 2 + MIDDLE_LINE_SPACING)) + MIDDLE_LINE_SPACING
      pygame.draw.rect(self.window, COLOR_LIGHT_GREY, (x, y, MIDDLE_LINE_WIDTH, MIDDLE_LINE_HEIGHT))

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
    pygame.draw.rect(self.window, COLOR_WHITE, (player.x, player.y, player.width, player.height))

  def _draw_ball(self):
    ball = self.game.ball
    pygame.draw.circle(self.window, COLOR_ORANGE, (ball.x, ball.y), ball.width)