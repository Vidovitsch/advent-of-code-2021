import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 11 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '1656'
      }
    ]
  )

def run():
  get_puzzle().run_tests_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  return input

if __name__ == '__main__':
  run()
