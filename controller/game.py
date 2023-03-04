import pygame
from controller.consts import BALL_MAX_VELOCITY, BALL_RADIUS, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN, WINNING_SCORE
from models.Player import Player
from models.Ball import Ball
from consts import WINDOW_WIDTH, WINDOW_HEIGHT

class Game:
  def __init__(self):
    self._init_players()
    self._init_ball()

  def play_turn(self):
    self._move_players()
    self._move_ball()
    self._handle_collision()
    self._update_score()
  
  def get_winner(self):
    if self.player_one.score == WINNING_SCORE:
      return self.player_one
    elif self.player_two.score == WINNING_SCORE:
      return self.player_two
    
    return None

  def _init_players(self):
    x = SCREEN_EDGE_MARGIN
    y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

    self.player_one = Player('Ronaldo', 0, x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    x = WINDOW_WIDTH - SCREEN_EDGE_MARGIN - PLAYER_WIDTH

    self.player_two = Player('Messi', 0, x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

  def _init_ball(self):
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2

    self.ball = Ball(x, y, BALL_RADIUS, BALL_MAX_VELOCITY)

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
    self._handle_collision_with_window()
    self._handle_collision_with_player_one()
    self._handle_collision_with_player_two()
  
  def _handle_collision_with_window(self):
    ball = self.ball
    if (ball.y + ball.radius >= WINDOW_HEIGHT) or (ball.y - ball.radius <= 0):
      ball.y_velocity *= -1
  
  def _handle_collision_with_player_one(self):
    ball = self.ball
    player_one = self.player_one

    if ball.x_velocity < 0:
      if ball.y >= player_one.y and ball.y <= player_one.y + player_one.height:
        if ball.x - ball.radius <= player_one.x + player_one.width:
          self._change_ball_speed(player_one)

  def _handle_collision_with_player_two(self):
    ball = self.ball
    player_two = self.player_two

    if ball.x_velocity > 0:
      if ball.y >= player_two.y and ball.y <= player_two.y + player_two.height:
        if ball.x + ball.radius >= player_two.x:
          self._change_ball_speed(player_two)
  
  def _change_ball_speed(self, player):
    ball = self.ball

    ball.x_velocity *= -1

    middle_y = player.y + player.height / 2
    difference_y = middle_y - ball.y
    reduction_factor = (player.height / 2) / BALL_MAX_VELOCITY
    y_velocity = difference_y / reduction_factor
    ball.y_velocity = -1 * y_velocity

  def _update_score(self):
    if self.ball.x < 0:
      self.player_one.score += 1
      self._reset_status()
    elif self.ball.x > WINDOW_WIDTH:
      self.player_two.score += 1
      self._reset_status()

  def _reset_status(self):
    self.ball.reset()
    self.player_one.reset()
    self.player_two.reset()