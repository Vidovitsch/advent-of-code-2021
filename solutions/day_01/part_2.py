import pathlib
from typing import Any, List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

def process_input(input: List[str]) -> List[int]:
  return [int(line) for line in input]

@process_puzzle_input(process_input)
def solve(input: List[int]) -> int:
  count = 0
  index = 0
  previous_sum = None
  while index < len(input) - 2:
    sum = input[index] + input[index + 1] + input[index + 2]
    if previous_sum and sum > previous_sum:
      count +=1
    previous_sum = sum
    index += 1
  return count

if __name__ == '__main__':
  (Puzzle('Day 1 - Part 2', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 5 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 1858 })
    .solve(solve))