import pygame
from ui.ui import UI
from controller.game import Game

def main():
  pygame.font.init()
  pygame.mixer.init()

  game = Game()
  ui = UI(game)

  while True:
    ui.draw_window()

if __name__ == '__main__':
  main()
