import pygame
from ai.Train import Train
from models.model_factory import create_ball, create_player_one
from models.players.PlayerType import PlayerType


def main():
  pygame.font.init()
  pygame.mixer.init()

  ball = create_ball()
  player_one = create_player_one(PlayerType.BOSS_BOT, ball)

  train = Train(player_one, ball)
  train.neat()

if __name__ == '__main__':
  main()