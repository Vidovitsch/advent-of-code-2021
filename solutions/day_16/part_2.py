import pathlib
from typing import Any, List

from advent_helper.puzzle import Puzzle, PuzzleInput

def solve(input: PuzzleInput) -> Any:
  return len(input)

def process_input(input: List[str]) -> PuzzleInput:
  return input

if __name__ == '__main__':
  (Puzzle('Day 16 - Part 2', pathlib.Path(__file__).parent / 'input.txt')
    .set_input_processor(process_input)
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': -1 })
    .solve(solve))
