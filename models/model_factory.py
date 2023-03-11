import os
import pygame
from consts import BALL_INITIAL_VELOCITY, BALL_RADIUS, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN, WINDOW_HEIGHT, WINDOW_WIDTH
from models.players.AIPlayer import AIPlayer
from models.Ball import Ball
from models.players.BossBotPlayer import BossBotPlayer
from models.players.BotPlayer import BotPlayer
from models.players.HumanPlayer import HumanPlayer
from models.players.PlayerType import PlayerType


def create_player_one(player_type, ball):
  x = SCREEN_EDGE_MARGIN
  y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

  return _create_player(x, y, player_type, pygame.K_w, pygame.K_s, ball)

def create_player_two(player_type, ball):
  x = WINDOW_WIDTH - SCREEN_EDGE_MARGIN - PLAYER_WIDTH
  y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

  return _create_player(x, y, player_type, pygame.K_UP, pygame.K_DOWN, ball)

def create_ball():
  x = WINDOW_WIDTH / 2
  y = WINDOW_HEIGHT / 2

  return Ball(x, y, BALL_RADIUS, BALL_INITIAL_VELOCITY)

def _create_player(x, y, player_type, key_up, key_down, ball):
  match player_type:
    case PlayerType.HUMAN:
      return HumanPlayer('Human', 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, key_up, key_down)
    case PlayerType.BOT:
      return BotPlayer('Bot', 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, ball)
    case PlayerType.BOSS_BOT:
      return BossBotPlayer('Boos Bot', 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, ball)
    case _:
      return AIPlayer('AI', 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, ball)