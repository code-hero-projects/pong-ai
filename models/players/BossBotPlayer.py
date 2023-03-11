from models.players.BasePlayer import BasePlayer


class BossBotPlayer(BasePlayer):
  PADDLE_EDGE_MARGIN = 1

  def __init__(self, name, score, x, y, velocity, width, height, ball):
    super().__init__(name, score, x, y, velocity, width, height)
    self.ball = ball
  
  def move(self):
    end_y = self.y + self.height
    upper_middle_y = self.y + self.PADDLE_EDGE_MARGIN
    downer_middle_y = end_y - self.PADDLE_EDGE_MARGIN
    middle_y = self.y + self.height / 2

    if (self.ball.y < middle_y and self.ball.y > upper_middle_y) or self.ball.y > end_y:
      super()._move_down()
    elif (self.ball.y > middle_y and self.ball.y < downer_middle_y) or self.ball.y < self.y:
      super()._move_up()