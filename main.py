import pygame
from consts import FPS
from ui.ui import UI
from controller.game import Game

def main():
  pygame.font.init()
  pygame.mixer.init()
  pygame.init()

  game = Game()
  ui = UI(game)

  clock = pygame.time.Clock()
  run = True

  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    game.play_turn()
    ui.draw_window()
  
  pygame.quit()

if __name__ == '__main__':
  main()
