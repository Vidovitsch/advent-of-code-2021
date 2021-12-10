import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 10 - Part 2',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '288957'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

CLOSING_CHARS = {
  ')': { 'points': 1, 'opening_char': '(' },
  ']': { 'points': 2, 'opening_char': '[' },
  '}': { 'points': 3, 'opening_char': '{' },
  '>': { 'points': 4, 'opening_char': '<' },
}

OPENING_CHARS = {
  '(': ')',
  '[': ']',
  '{': '}',
  '<': '>'
}

def solve(input):
  scores = []

  for line in input:
    points = 0
    corrupted = False
    stack = []

    for char in line:
      if char in CLOSING_CHARS and CLOSING_CHARS[char]['opening_char'] == stack[len(stack) - 1]:
        stack.pop()
      elif char in CLOSING_CHARS:
        corrupted = True
        break
      else:
        stack.append(char)

    if corrupted:
      continue

    for char in ''.join(reversed([OPENING_CHARS[char] for char in stack])):
      points = points * 5 + CLOSING_CHARS[char]['points']
    scores.append(points)

  return sorted(scores)[int((len(scores) - 1) / 2)]

if __name__ == '__main__':
  run()
