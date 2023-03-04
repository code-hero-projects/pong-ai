from controller.consts import WINNING_SCORE
from consts import BALL_INITIAL_VELOCITY, WINDOW_WIDTH, WINDOW_HEIGHT

class Game:
  def __init__(self, player_one, player_two, ball):
    self.player_one = player_one
    self.player_two = player_two
    self.ball = ball

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

  def _move_players(self):
    self.player_one.move()
    self.player_two.move()
  
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
    reduction_factor = (player.height / 2) / BALL_INITIAL_VELOCITY
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