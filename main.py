import time
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
  run = True

  while run:
    clock.tick(FPS)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    game.play_turn()
    ui.draw_window()
  
    winner = game.get_winner()
    if winner != None:
      ui.draw_game_over(winner)
      run = False
      time.sleep(5)

  pygame.quit()

if __name__ == '__main__':
  main()
