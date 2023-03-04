import pygame
from consts import FPS
from ui.ui import UI
from controller.game import Game

def main():
  pygame.font.init()
  pygame.mixer.init()

  game = Game()
  ui = UI(game)

  clock = pygame.time.Clock()
  while True:
    clock.tick(FPS)
    ui.draw_window()

if __name__ == '__main__':
  main()
