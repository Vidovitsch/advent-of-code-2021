import pathlib

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 2- Part 2',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '900'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '1604592846'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve, run_tests=True)

##############################################################
# Solution
##############################################################

def solve(input):
  x = 0
  y = 0
  aim = 0
  for course in input:
    direction, amount = course.split()
    match direction:
      case 'forward':
        x += int(amount)
        y += aim * int(amount)
      case 'down':
        aim += int(amount)
      case 'up':
        aim -= int(amount)
  return x * y

if __name__ == '__main__':
  run()
