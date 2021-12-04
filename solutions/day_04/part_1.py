import pathlib
import collections

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 4 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '4512'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  bingo_numbers = create_bingo_numbers(input)
  bingo_cards = create_bingo_cards(input)
  
  for number in bingo_numbers:
    for card in bingo_cards:
      if card.mark_number(number):
        return calculate_solution(card, number)

  return None

def calculate_solution(card, number):
  return sum([int(num) for num in list(card.unmarked_grid.keys())]) * int(number)

def create_bingo_numbers(input):
  return input[0].split(',')

def create_bingo_cards(input):
  cleaned_input = [row.split() for row in input[1:]]

  return [BingoCard(cleaned_input[i:i + 5]) for i in range(0, len(cleaned_input), 5)]

class BingoCard:
  def __init__(self, grid):
    self.unmarked_grid = self._prepare_grid(grid)
    self.marked_grid = {}

  def mark_number(self, number):
    if number in self.unmarked_grid:
      self.marked_grid[number] = self.unmarked_grid[number]
      del self.unmarked_grid[number]

    if len(self.marked_grid) >= 5:
      return self.hasBingo()

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
  run()
