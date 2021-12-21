import pathlib
from typing import Any, List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[int]

def process_input(input: List[str]) -> PuzzleInput:
  return [int(line.split(': ')[1]) for line in input]

class Game:
  def __init__(self, player_positions, die_sides=100, track_size=10, winning_score=1000):
    self.die_sides = die_sides
    self.player_positions = player_positions
    self.track_size = track_size
    self.winning_score = winning_score

    self.player_scores = [0] * len(player_positions)
    self.previous_die_roll = None
    self.die_roll_count = 0
    self.current_player = 0

  def play(self) -> int:
    while True:
      rolled_value = sum(self.roll_die() for _ in range(3))
      self.move_player(rolled_value)

      if self.player_scores[self.current_player] >= self.winning_score:
        return min(self.player_scores) * self.die_roll_count

      self.next_turn()

  def next_turn(self):
    self.current_player = (self.current_player + 1) % len(self.player_positions)
    return 
  
  def move_player(self, value: int):
    self.player_positions[self.current_player] = (self.player_positions[self.current_player] + value) % self.track_size or self.track_size
    self.player_scores[self.current_player] += self.player_positions[self.current_player]

  def roll_die(self) -> int:
    if not self.previous_die_roll:
      self.previous_die_roll = 1
    else:
      self.previous_die_roll = (self.previous_die_roll + 1) % self.die_sides or self.die_sides

    self.die_roll_count += 1

    return self.previous_die_roll

@process_puzzle_input(process_input)
def solve(player_positions: PuzzleInput) -> int:
  game = Game(player_positions)

  return game.play()

if __name__ == '__main__':
  (Puzzle('Day 21: Dirac Dice - part 1', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 739785 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 551901 })
    .solve(solve))
