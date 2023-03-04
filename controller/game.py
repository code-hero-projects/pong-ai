import pygame
from controller.consts import BALL_VELOCITY, BALL_RADIUS, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN
from models.Player import Player
from models.Ball import Ball
from consts import WINDOW_WIDTH, WINDOW_HEIGHT

class Game:
  def __init__(self):
    self._init_players()
    self._init_ball()
  
  def _init_players(self):
    x = SCREEN_EDGE_MARGIN
    y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

    self.player_one = Player('Ronaldo', 0, x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    x = WINDOW_WIDTH - SCREEN_EDGE_MARGIN - PLAYER_WIDTH

    self.player_two = Player('Messi', 0, x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

  def _init_ball(self):
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2

    self.ball = Ball(x, y, BALL_RADIUS, BALL_VELOCITY)

  def play_turn(self):
    self._move_players()
    self._move_ball()
    self._handle_collision()
  
  def _move_players(self):
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_w]:
      self.player_one.move_up(PLAYER_VELOCITY)
    elif keys_pressed[pygame.K_s]:
      self.player_one.move_down(PLAYER_VELOCITY)
    elif keys_pressed[pygame.K_UP]:
      self.player_two.move_up(PLAYER_VELOCITY)
    elif keys_pressed[pygame.K_DOWN]:
      self.player_two.move_down(PLAYER_VELOCITY)
  
  def _move_ball(self):
    self.ball.move()
  
  def _handle_collision(self):
    ball = self.ball
    player_one = self.player_one
    player_two = self.player_two

    # collision with up and lower bounds
    if (ball.y + ball.radius >= WINDOW_HEIGHT) or (ball.y - ball.radius <= 0):
      ball.y_velocity *= -1


    # check collision with left player
    if ball.x_velocity < 0:
      if ball.y >= player_one.y and ball.y <= player_one.y + player_one.height:
        if ball.x - ball.radius <= player_one.x + player_one.width:
          ball.x_velocity *= -1
    # check collision with right player
    else:
      if ball.y >= player_two.y and ball.y <= player_two.y + player_two.height:
        if ball.x + ball.radius >= player_two.x:
          ball.x_velocity *= -1
  