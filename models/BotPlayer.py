from models.BasePlayer import BasePlayer


class BotPlayer(BasePlayer):
  def __init__(self, name, score, x, y, velocity, width, height, ball):
    super().__init__(name, score, x, y, velocity, width, height)
    self.ball = ball
  
  def move(self):
    middle_y = self.y + self.height / 2
    if self.ball.y > middle_y:
      super()._move_down()
    else:
      super()._move_up()