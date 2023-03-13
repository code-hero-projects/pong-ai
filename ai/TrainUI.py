import pygame
from consts import WINDOW_WIDTH
from ui.consts import COLOR_WHITE, FONT, FONT_MARGIN_TOP
from ui.ui import UI


class TrainUI(UI):

  def __init__(self, game, player_one_ai):
    super().__init__(game)
    self.player_one_ai = player_one_ai

  def _draw_score(self):
    score_font = pygame.font.SysFont(FONT, 100)

    middle = WINDOW_WIDTH / 2

    player_one_score_text = f'{self.game.player_one.name}'

    if (self.player_one_ai):
      player_one_score_text = player_one_score_text + f', Hits - {self.game.player_one.hits}'

    score = score_font.render(player_one_score_text, 1, COLOR_WHITE)

    start_x = (middle - score.get_width()) / 2
    self.window.blit(score, (start_x, FONT_MARGIN_TOP))

    player_two_score_text = f'{self.game.player_two.name}, Hits - {self.game.player_two.hits}'

    score = score_font.render(player_two_score_text, 1, COLOR_WHITE)

    start_x = middle + ((middle - score.get_width()) / 2)
    self.window.blit(score, (start_x, FONT_MARGIN_TOP))
