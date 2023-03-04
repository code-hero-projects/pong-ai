import pygame
import os

from assets.consts import PLAYER_IMAGE, MIDDLE_LINE_IMAGE
from models.ImageAsset import ImageAsset

def get_player():
  return _get_image_asset(PLAYER_IMAGE)

def get_middle_line():
  return _get_image_asset(MIDDLE_LINE_IMAGE)

def _get_image_asset(image_path):
  image = pygame.image.load(os.path.join(image_path))
  image_width = image.get_width()
  image_height = image.get_height()

  return ImageAsset(image, image_width, image_height)