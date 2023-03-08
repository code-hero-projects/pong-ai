import neat
import pygame
from ai.AIPlayer import AIPlayer
from consts import BALL_INITIAL_VELOCITY, PLAYER_HEIGHT, PLAYER_VELOCITY, PLAYER_WIDTH, SCREEN_EDGE_MARGIN, WINDOW_HEIGHT, WINDOW_WIDTH
from controller.consts import FPS

from ui.ui import UI
from models.PlayerType import PlayerType
from models.model_factory import create_ball, create_player_one, create_player_two

class Train:
  def __init__(self):
    self.ball = create_ball()
    self.player_one = create_player_one(PlayerType.BOT, self.ball)
    self.ui = UI(self)

  def neat(self, config_file, generation=None):
    if not generation:
      config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_file)
      population = neat.Population(config)
    else:
      population = neat.Checkpointer.restore_checkpoint('neat-checkpoint-15')
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    population.add_reporter(neat.Checkpointer(1))

    winner = population.run(self._evaluate_genomes, 50)

  def _evaluate_genomes(self, genomes, config):
    for i, (genome_id, genome) in enumerate(genomes):
      genome.fitness = 0 if genome.fitness == None else genome.fitness
      generation = i // 50
      self._train_ai(generation, genome, config)

  def _train_ai(self, generation, genome, config):
    clock = pygame.time.Clock()
    run = True

    neural_network = neat.nn.FeedForwardNetwork.create(genome, config)
    self.player_two = self._create_ai_player(generation, genome, neural_network)
    
    while run:
      clock.tick(FPS)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False

      self._play_turn()
      self.ui.draw_window()

      if self.player_one.score == 1 or self.player_two.score == 1:
        genome.fitness += self.player_two.hits + self.player_two.score * 2
        self._reset_scores()
        break

  def _create_ai_player(self, generation, genome, neural_network):
    x = WINDOW_WIDTH - SCREEN_EDGE_MARGIN - PLAYER_WIDTH
    y = WINDOW_HEIGHT / 2 - PLAYER_HEIGHT / 2

    player_name = f'Gen #{generation}'

    return AIPlayer(player_name, 0, x, y, PLAYER_VELOCITY, PLAYER_WIDTH, PLAYER_HEIGHT, self.ball, neural_network, genome)

  def _play_turn(self):
    self._move_players()
    self._move_ball()
    self._handle_collision()
    self._update_score()

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

    player.hits += 1

  def _update_score(self):
    if self.ball.x < 0:
      self.player_two.score += 1
      self._reset_status()
    elif self.ball.x > WINDOW_WIDTH:
      self.player_one.score += 1
      self._reset_status()

  def _reset_status(self):
    self.ball.reset()
    self.player_one.reset()
    self.player_two.reset()
  
  def _reset_scores(self):
    self.player_one.score = 0
    self.player_two_score = 0