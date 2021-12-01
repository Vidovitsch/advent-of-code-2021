import pathlib

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 2- Part 2',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': ''
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve, run_tests=True)

##############################################################
# Solution
##############################################################

def solve(input):
  return None

if __name__ == '__main__':
  run()
