import pygame
from controller.consts import PLAYER_VELOCITY
from models.Player import Player
from models.Ball import Ball
from ui.consts import WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN_EDGE_MARGIN
from assets.assets import get_player

class Game:
  def __init__(self):
    self._init_players()
    self._init_ball()

    self.keys_functions = {
      pygame.K_w: self.player_one.move_up,
      pygame.K_s: self.player_one.move_down,
      pygame.K_UP: self.player_two.move_up,
      pygame.K_DOWN: self.player_two.move_down
    }
  
  def _init_players(self):
    player_image = get_player()
    y = WINDOW_HEIGHT / 2 - player_image.height / 2

    player_one_location = (0 + SCREEN_EDGE_MARGIN, y)
    self.player_one = Player('Ronaldo', 0, player_one_location)

    player_two_location = (WINDOW_WIDTH - SCREEN_EDGE_MARGIN - player_image.width, y)
    self.player_two = Player('Messi', 0, player_two_location)

  def _init_ball(self):
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2

    self.ball = Ball((x, y))

  def play_turn(self):
    keys_pressed = pygame.key.get_pressed()

    for key in self.keys_functions:
      if keys_pressed[key]:
        move_player = self.keys_functions[key]
        move_player(PLAYER_VELOCITY)