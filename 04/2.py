import pathlib
from typing import Any, List

from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[str]

def solve(input: PuzzleInput) -> Any:
  bingo_numbers = create_bingo_numbers(input)
  bingo_cards = create_bingo_cards(input)
  
  winning_results = []
  for number in bingo_numbers:
    for card in bingo_cards:
      if result := card.mark_number(number):
        winning_results.append(result)

  return winning_results[-1]

def create_bingo_numbers(input):
  return input[0].split(',')

def create_bingo_cards(input):
  cleaned_input = [row.split() for row in input[1:]]

  return [BingoCard(cleaned_input[i:i + 5]) for i in range(0, len(cleaned_input), 5)]

class BingoCard:
  def __init__(self, grid):
    self.has_already_won = False
    self.unmarked_grid = self._prepare_grid(grid)
    self.marked_grid = {}

  def mark_number(self, number):
    if number in self.unmarked_grid:
      self.marked_grid[number] = self.unmarked_grid[number]
      del self.unmarked_grid[number]

    if len(self.marked_grid) >= 5 and self.hasBingo() and not self.has_already_won:
      self.has_already_won = True
      return sum([int(num) for num in self.unmarked_grid.keys()]) * int(number)

    return False

  def hasBingo(self):
    x_count = [0] * 5
    y_count = [0] * 5

    for x, y in self.marked_grid.values():
      x_count[x] += 1
      y_count[y] += 1
      if x_count[x] == 5 or y_count[y] == 5:
        return True

    return False
  
  def _prepare_grid(self, grid):
    prepared_grid = dict()

    for y, row in enumerate(grid):
      for x, number in enumerate(row):
        prepared_grid[number] = [x, y]
    
    return prepared_grid

if __name__ == '__main__':
  (Puzzle('Day 4: Giant Squid (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 1924 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 2730 })
    .solve(solve))
