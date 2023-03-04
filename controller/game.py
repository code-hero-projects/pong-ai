from models.Player import Player
from models.Point import Point
from ui.consts import WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN_EDGE_MARGIN
from assets.assets import get_player

class Game:
  def __init__(self):
    self._init_players()
    self.ball = None
    self.score = []
  
  def _init_players(self):
    player_image = get_player()
    y = WINDOW_HEIGHT / 2 - player_image.height / 2

    player_one_location = Point(0 + SCREEN_EDGE_MARGIN, y)
    self.player_one = Player('Ronaldo', 0, player_one_location)

    player_two_location = Point(WINDOW_WIDTH - SCREEN_EDGE_MARGIN - player_image.width, y)
    self.player_two = Player('Messi', 0, player_two_location)