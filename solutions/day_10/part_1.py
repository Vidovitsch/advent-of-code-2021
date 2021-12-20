import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 10 - Part 1',
    CURRENT / 'input.txt',
    [
      {
        'input_path': CURRENT / 'test.txt',
        'expected_result': '26397'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

CLOSING_CHARS = {
  ')': { 'points': 3, 'opening_char': '(' },
  ']': { 'points': 57, 'opening_char': '[' },
  '}': { 'points': 1197, 'opening_char': '{' },
  '>': { 'points': 25137, 'opening_char': '<' },
}
def solve(input):
  points = 0

  for line in input:
    stack = []
    for char in line:
      if char in CLOSING_CHARS and CLOSING_CHARS[char]['opening_char'] == stack[len(stack) - 1]:
        stack.pop()
      elif char in CLOSING_CHARS:
        points += CLOSING_CHARS[char]['points']
        break
      else:
        stack.append(char)

  return points

if __name__ == '__main__':
  run()
