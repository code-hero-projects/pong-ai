import pygame
from ai.AITrain import AITrain
from ai.BotTrain import BotTrain
from models.model_factory import create_ball, create_player_one
from models.players.PlayerType import PlayerType


def main():
  pygame.font.init()
  pygame.mixer.init()

  ball = create_ball()
  player_one = create_player_one(PlayerType.BOSS_BOT, ball)

  # train = BotTrain(ball, player_one)
  train = AITrain(ball)
  train.neat()

if __name__ == '__main__':
  main()