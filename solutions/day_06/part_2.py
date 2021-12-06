import pathlib
from collections import deque

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 6 - Part 2',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '26984457539'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '1708791884591'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  days = 256
  internal_timers = get_internal_timers(input) # index = timer, value = amount of fish

  for i in range(days):
    internal_timers.rotate(-1)
    internal_timers[6] += internal_timers[8]

  return sum(internal_timers)

def get_internal_timers(input):
  internal_timers = [0] * 9

  for timer in input[0].split(','):
    internal_timers[int(timer)] += 1

  return deque(internal_timers)

if __name__ == '__main__':
  run()
