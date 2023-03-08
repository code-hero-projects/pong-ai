import pygame

from ui.consts import COLOR_BLACK, COLOR_LIGHT_GREY, COLOR_ORANGE, FONT_MARGIN_TOP, MIDDLE_LINE_HEIGHT, MIDDLE_LINE_SPACING, FONT, COLOR_WHITE, MIDDLE_LINE_WIDTH
from consts import WINDOW_HEIGHT, WINDOW_WIDTH

class UI:
  def __init__(self, game, draw_hits=False):
    self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    self.game = game
    self.draw_hits = draw_hits
  
  def draw_window(self):
    self.window.fill(COLOR_BLACK)

    self._draw_middle_line()
    self._draw_score()
    self._draw_players()
    self._draw_ball()

    pygame.display.update()
  
  def draw_game_over(self, player):
    self.draw_window()

    text = f'GAME OVER'
    # text = f'{player.name} has won! Congratulations!'
    winner_font = pygame.font.SysFont(FONT, 200)
    winner = winner_font.render(text, 1, COLOR_WHITE)
    self.window.blit(winner, (WINDOW_WIDTH / 2 - winner.get_width() / 2, WINDOW_HEIGHT / 2 - winner.get_height() / 2))

    pygame.display.update()

  def _draw_middle_line(self):    
    x = WINDOW_WIDTH / 2 - MIDDLE_LINE_WIDTH / 2
    for middle_line_counter in range(10):
      y = (middle_line_counter * (MIDDLE_LINE_HEIGHT * 2 + MIDDLE_LINE_SPACING)) + MIDDLE_LINE_SPACING
      pygame.draw.rect(self.window, COLOR_LIGHT_GREY, (x, y, MIDDLE_LINE_WIDTH, MIDDLE_LINE_HEIGHT))

  def _draw_score(self):
    score_font = pygame.font.SysFont(FONT, 100)

    player_one_score_text = f'{self.game.player_one.name} - {self.game.player_one.score}'
    score = score_font.render(player_one_score_text, 1, COLOR_WHITE)
    self.window.blit(score, (WINDOW_WIDTH / 2 - score.get_width() * 2, FONT_MARGIN_TOP))

    player_two_score_text = f'{self.game.player_two.name} - {self.game.player_two.score}'

    if (self.draw_hits):
      player_two_score_text = player_two_score_text + f', Hits - {self.game.player_two.hits}'

    score = score_font.render(player_two_score_text, 1, COLOR_WHITE)
    self.window.blit(score, (WINDOW_WIDTH / 2 + 50, FONT_MARGIN_TOP))

  def _draw_players(self):
    self._draw_player(self.game.player_one)
    self._draw_player(self.game.player_two)

  def _draw_player(self, player):
    pygame.draw.rect(self.window, COLOR_WHITE, (player.x, player.y, player.width, player.height))

  def _draw_ball(self):
    ball = self.game.ball
    pygame.draw.circle(self.window, COLOR_ORANGE, (ball.x, ball.y), ball.radius)