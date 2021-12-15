import pathlib
from typing import Any, List

from advent_helper.puzzle import Puzzle, PuzzleInput

def solve(input: PuzzleInput) -> Any:
  previous_measurement = None
  count = 0
  for measurement in input:
    if previous_measurement and previous_measurement < measurement:
      count += 1
    previous_measurement = measurement

  return count

def process_input(input: List[str]) -> PuzzleInput:
  return [int(line) for line in input]

if __name__ == '__main__':
  (Puzzle('Day 1 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .set_input_processor(process_input)
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 7 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 1832 })
    .solve(solve))