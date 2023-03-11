import pygame
from ai.Train import Train


def main():
  pygame.font.init()
  pygame.mixer.init()

  train = Train()
  train.neat()

if __name__ == '__main__':
  main()