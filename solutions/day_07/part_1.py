import math
import pathlib
from typing import Any, List

from advent_helper.puzzle import Puzzle, PuzzleInput

def solve(locations: PuzzleInput) -> Any:
  min_fuel = math.inf
  for i in range(max(locations)):
    fuel = sum(abs(i - location) for location in locations)
    if fuel < min_fuel:
      min_fuel = fuel
  
  return min_fuel

def process_input(input: List[str]) -> PuzzleInput:
  return list(map(int, input[0].split(',')))

if __name__ == '__main__':
  (Puzzle('Day 7 - Part 1', CURRENT / 'input.txt')
    .set_input_processor(process_input)
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 37 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 355592 })
    .solve(solve))
