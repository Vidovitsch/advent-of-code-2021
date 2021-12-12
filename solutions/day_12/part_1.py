import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 12 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test1.txt',
        'expected_result': '10'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'test2.txt',
        'expected_result': '19'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'test3.txt',
        'expected_result': '226'
      }
    ]
  )

def run():
  get_puzzle().run_tests_with(solve, process_input)

##############################################################
# Solution
##############################################################

def process_input(line):
  return line

def solve(input):
  return input

if __name__ == '__main__':
  run()
