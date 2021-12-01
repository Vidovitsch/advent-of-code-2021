import pathlib

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 1 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '7'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve, run_tests=True)

##############################################################
# Solution
##############################################################

def solve(input):
  input = [int(i) for i in input]
  previous_measurement = None
  count = 0
  for measurement in input:
    if previous_measurement and previous_measurement < measurement:
      count += 1
    previous_measurement = measurement

  return count

if __name__ == '__main__':
  run()