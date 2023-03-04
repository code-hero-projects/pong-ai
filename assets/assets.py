import pygame
import os

from assets.consts import PLAYER_IMAGE

def get_player():
  return pygame.image.load(os.path.join(PLAYER_IMAGE))