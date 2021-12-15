import pathlib
from typing import Any, List

from advent_helper.puzzle import Puzzle, PuzzleInput

def solve(input: PuzzleInput) -> Any:
  x = 0
  y = 0
  for course in input:
    direction, amount = course.split()
    match direction:
      case 'forward':
        x += int(amount)
      case 'down':
        y += int(amount)
      case 'up':
        y -= int(amount)
  return x * y

if __name__ == '__main__':
  (Puzzle('Day 2 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 150 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 1660158 })
    .solve(solve))
