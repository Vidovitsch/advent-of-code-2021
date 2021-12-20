import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 8 - Part 1',
    CURRENT / 'input.txt',
    [
      {
        'input_path': CURRENT / 'test.txt',
        'expected_result': '26'
      },
      {
        'input_path': CURRENT / 'input.txt',
        'expected_result': '504'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  entries = get_entries(input)

  count = 0
  for entry in entries:
    for signal in entry[1]:
      if len(signal) in [2, 3, 4, 7]:
        count += 1

  return count

def get_entries(input):
  entries = []

  for line in input:
    signal_patterns, output_value = line.split(' | ')
    entries.append([signal_patterns.split(), output_value.split()])

  return entries



if __name__ == '__main__':
  run()
