import pathlib
from typing import Any, List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[str]

def process_input(input: List[str]) -> PuzzleInput:
  return input

@process_puzzle_input(process_input)
def solve(input: PuzzleInput) -> int:
  return len(input)

if __name__ == '__main__':
  (Puzzle('Day 21: Trench Map - part 1', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': '???' })
    .solve(solve))
