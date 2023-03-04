import pygame
from controller.consts import BALL_WIDTH, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN
from models.Player import Player
from models.Ball import Ball
from consts import WINDOW_WIDTH, WINDOW_HEIGHT

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
    x = SCREEN_EDGE_MARGIN
    y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

    self.player_one = Player('Ronaldo', 0, x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    x = WINDOW_WIDTH - SCREEN_EDGE_MARGIN - PLAYER_WIDTH

    self.player_two = Player('Messi', 0, x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

  def _init_ball(self):
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2

    self.ball = Ball(x, y, BALL_WIDTH)

  def play_turn(self):
    keys_pressed = pygame.key.get_pressed()

    for key in self.keys_functions:
      if keys_pressed[key]:
        move_player = self.keys_functions[key]
        move_player(PLAYER_VELOCITY)