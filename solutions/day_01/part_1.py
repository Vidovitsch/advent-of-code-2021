import pathlib
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

def process_input(input: List[str]) -> List[int]:
  return [int(i) for i in input]

@process_puzzle_input(process_input)
def solve(input: List[int]) -> int:
  previous_measurement = None
  count = 0
  for measurement in input:
    if previous_measurement and previous_measurement < measurement:
      count += 1
    previous_measurement = measurement

  return count

if __name__ == '__main__':
  (Puzzle('Day 1 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 7 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 1832 })
    .solve(solve))
