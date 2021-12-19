import pathlib
from typing import List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

def process_input(input: List[str]) -> List[str]:
  return [eval(line) for line in input]

@process_puzzle_input(process_input)
def solve(input: List[str]) -> int:
  return 0

if __name__ == '__main__':
  (Puzzle('Day 19 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 0 })
    .solve(solve))
