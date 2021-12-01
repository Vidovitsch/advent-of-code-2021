import pathlib

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 1 - Part 2',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '5'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '1858'
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
  count = 0
  index = 0
  previous_sum = None
  while index < len(input) - 2:
    sum = input[index] + input[index + 1] + input[index + 2]
    if previous_sum and sum > previous_sum:
      count +=1
    previous_sum = sum
    index += 1
  return count

if __name__ == '__main__':
  run()