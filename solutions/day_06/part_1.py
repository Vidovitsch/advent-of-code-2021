import pathlib
from collections import deque

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 6 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '5934'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '380243'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  days = 80
  internal_timers = get_internal_timers(input)

  for i in range(days):
    new_fish_to_add = internal_timers[0]
    internal_timers.rotate(-1)
    internal_timers[6] += internal_timers[8]
    internal_timers[8] = new_fish_to_add

  return sum(internal_timers)

def get_internal_timers(input):
  internal_timers = [0] * 9

  for timer in input[0].split(','):
    internal_timers[int(timer)] += 1

  return deque(internal_timers)

if __name__ == '__main__':
  run()
