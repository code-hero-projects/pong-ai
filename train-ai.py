import os
import pygame
from ai.Train import Train


def main():
  pygame.font.init()
  pygame.mixer.init()

  local_dir = os.path.dirname(__file__)
  config_path = os.path.join(local_dir, 'neat_config.txt')

  train = Train()
  train.neat(config_path)

if __name__ == '__main__':
  main()