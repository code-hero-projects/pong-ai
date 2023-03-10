import pygame
from models.PlayerType import PlayerType
from models.model_factory import create_ball, create_player_one, create_player_two
from controller.game import Game

def main():
  pygame.font.init()
  pygame.mixer.init()

  ball = create_ball()
  player_one = create_player_one(PlayerType.BOT, ball)
  player_two = create_player_two(PlayerType.AI, ball)

  game = Game(player_one, player_two, ball)

  game.play()

  pygame.quit()

if __name__ == '__main__':
  main()
