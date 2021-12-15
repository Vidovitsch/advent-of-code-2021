import collections
import pathlib
from typing import Any, List

from advent_helper.puzzle import Puzzle, PuzzleInput

def solve(input: PuzzleInput) -> Any:
  gamma_rate = ''
  epsilon_rate = ''

  bits = ''
  for i in range(len(input[0])):
    for number in input:
      bits += number[i]
    counter = collections.Counter(bits).most_common()
    gamma_rate += counter[0][0]
    epsilon_rate += counter[-1][0]
    bits = ''

  return int(gamma_rate, 2) * int(epsilon_rate, 2)

if __name__ == '__main__':
  (Puzzle('Day 3 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 198 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 1307354 })
    .solve(solve))

