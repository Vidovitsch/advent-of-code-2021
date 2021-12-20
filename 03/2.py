import collections
import pathlib
from typing import Any, List

from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[str]

def solve(input: PuzzleInput) -> Any:
  o_gen_rating = ''
  co2_scrub_rating = ''

  selection = select_for_most_common_first_bit(input, bit_index=0, tie_breaker='1')
  count = 0
  while len(selection) > 1:
    count += 1
    selection = select_for_most_common_first_bit(selection, bit_index=count, tie_breaker='1')
  o_gen_rating = selection[0]

  selection = select_for_most_common_first_bit(input, bit_index=0, tie_breaker='0')
  count = 0
  while len(selection) > 1:
    count += 1
    selection = select_for_most_common_first_bit(selection, bit_index=count, tie_breaker='0')
  co2_scrub_rating = selection[0]

  return int(o_gen_rating, 2) * int(co2_scrub_rating, 2)

def select_for_most_common_first_bit(numbers, bit_index=0, tie_breaker='1'):
  number = ''.join(number[bit_index] for number in numbers)

  counter = collections.Counter(number).most_common()
  most_common_bit = counter[0][0]
  least_common_bit = counter[-1][0]

  if tie_breaker == '0':
    most_common_bit = least_common_bit

  if counter[0][1] == counter[-1][1]:
    most_common_bit = tie_breaker

  selection = []
  for number in numbers:
    if number[bit_index] == most_common_bit:
      selection.append(number)
  return selection

if __name__ == '__main__':
  (Puzzle('Day 3: Binary Diagnostic (part 2)', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 230 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 482500 })
    .solve(solve))
