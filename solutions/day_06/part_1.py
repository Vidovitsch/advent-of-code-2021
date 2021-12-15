from collections import deque
import pathlib
from typing import Any, List

from advent_helper.puzzle import Puzzle, PuzzleInput

def solve(input: PuzzleInput) -> Any:
  days = 80
  internal_timers = get_internal_timers(input)

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
  (Puzzle('Day 6 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 5934 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 380243 })
    .solve(solve))
