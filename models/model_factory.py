import pygame
from consts import BALL_INITIAL_VELOCITY, BALL_RADIUS, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN, WINDOW_HEIGHT, WINDOW_WIDTH
from models.Ball import Ball
from models.Player import Player


def create_player_one(ai):
  x = SCREEN_EDGE_MARGIN
  y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

  if ai:
    return Player('Ronaldo', 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, pygame.K_q, pygame.K_a)
  
  return Player('Ronaldo', 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, pygame.K_w, pygame.K_s)

def create_player_two(ai):
  x = WINDOW_WIDTH - SCREEN_EDGE_MARGIN - PLAYER_WIDTH
  y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

  if ai:
    return Player('Messi', 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, pygame.K_p, pygame.K_l)
  
  return Player('Messi', 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, pygame.K_UP, pygame.K_DOWN)

def create_ball():
  x = WINDOW_WIDTH / 2
  y = WINDOW_HEIGHT / 2

  return Ball(x, y, BALL_RADIUS, BALL_INITIAL_VELOCITY)