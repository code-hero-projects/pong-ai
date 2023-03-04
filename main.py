import time
import pygame
from consts import FPS
from models.model_factory import create_ball, create_player_one, create_player_two
from ui.ui import UI
from controller.game import Game

def main():
  pygame.font.init()
  pygame.mixer.init()

  player_one = create_player_one(True)
  player_two = create_player_two(True)
  ball = create_ball()

  game = Game(player_one, player_two, ball)
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
