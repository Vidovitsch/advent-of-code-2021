import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 7 - Part 2',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '168'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '101618069'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  locations = list(map(int, input[0].split(',')))
  min_fuel = math.inf
  for i in range(max(locations)):
    fuel = sum(sum(range(abs(i - location) + 1)) for location in locations)
    if fuel < min_fuel:
      min_fuel = fuel
  
  return min_fuel

if __name__ == '__main__':
  run()
