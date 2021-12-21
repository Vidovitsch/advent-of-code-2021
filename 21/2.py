from collections import Counter
import pathlib
from typing import Any, List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[int]

def process_input(input: List[str]) -> PuzzleInput:
  return [int(line.split(': ')[1]) for line in input]

class Game:
  def __init__(self, player_positions, die_sides=3, track_size=10, winning_score=21, game_state={}):
    self.die_sides = die_sides
    self.player_positions = player_positions
    self.track_size = track_size
    self.winning_score = winning_score

    self.player_scores = [0] * len(player_positions) if not 'player_scores' in game_state else game_state['player_scores']
    self.rolled_value = 0 if not 'rolled_value' in game_state else game_state['rolled_value']
    self.rolls_left = 3 if not 'rolls_left' in game_state else game_state['rolls_left']
    self.current_player = 0 if not 'current_player' in game_state else game_state['current_player']

  def play(self) -> int:
    won_games = []
    while True:
      if self.rolls_left:
        for _ in range(self.rolls_left):
          won_games = [self.roll_die_with_value(i + 1) for i in range(self.die_sides)]

      self.move_player(self.rolled_value)

      if self.player_scores[self.current_player] >= self.winning_score:
        counter = Counter({})
        counter[self.current_player] = 1
        for won_game in won_games:
          counter += won_game
        return counter

      self.next_turn()

  def next_turn(self):
    self.rolled_value = 0
    self.rolls_left = 3
    self.current_player = (self.current_player + 1) % len(self.player_positions)
  
  def move_player(self, value: int):
    self.player_positions[self.current_player] = (self.player_positions[self.current_player] + value) % self.track_size or self.track_size
    self.player_scores[self.current_player] += self.player_positions[self.current_player]

  def roll_die_with_value(self, value) -> int:
    self.rolls_left -= 1

    return Game(
      [i for i in self.player_positions],
      self.die_sides,
      self.track_size,
      self.winning_score,
      {
        'player_scores': [i for i in self.player_scores],
        'rolled_value': self.rolled_value + value,
        'rolls_left': self.rolls_left,
        'current_player': self.current_player
      }
    ).play()

@process_puzzle_input(process_input)
def solve(player_positions: PuzzleInput) -> int:
  game = Game(player_positions)

  return game.play()

if __name__ == '__main__':
  (Puzzle('Day 21: Dirac Dice - part 2', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 444356092776315 })
    .solve(solve))
