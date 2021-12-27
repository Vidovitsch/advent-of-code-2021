import pathlib
from typing import List, Tuple

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[Tuple[int, Tuple[Tuple[int, int]]]]

def process_input(input: List[str]) -> PuzzleInput:
  return input

@process_puzzle_input(process_input)
def solve(input: PuzzleInput) -> int:
  return len(input)

if __name__ == '__main__':
  (Puzzle('Day 23: Amphipod - part 1', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 39 })
    .solve(solve))
