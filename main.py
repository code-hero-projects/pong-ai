import time
import pygame
from consts import FPS
from models.PlayerType import PlayerType
from models.model_factory import create_ball, create_player_one, create_player_two
from ui.ui import UI
from controller.game import Game

def main():
  pygame.font.init()
  pygame.mixer.init()

  player_one = create_player_one(PlayerType.BOT)
  player_two = create_player_two(PlayerType.Human)
  ball = create_ball()

  game = Game(player_one, player_two, ball)

  game.play()

  pygame.quit()

if __name__ == '__main__':
  main()
