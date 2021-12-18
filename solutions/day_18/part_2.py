import copy
from itertools import combinations
import json
import math
import pathlib
from typing import List, Union

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

def process_input(input: List[str]) -> List[str]:
  return [eval(line) for line in input]

def split(number):
  for i, elem in enumerate(number):
    if isinstance(elem, list):
      done = split(elem)
      if done:
        return done
    elif elem >= 10:
      number[i] = [math.floor(elem / 2), math.ceil(elem / 2)]
      return True

  return False

def explode(number):
  def get_exploded_pair(number, level=0):
    pair = []

    for i, elem in enumerate(number):
      if isinstance(elem, list):
        result, replaced = get_exploded_pair(elem, level + 1)
        if result and not replaced:
          number[i] = '#'
        if result:
          return result, True
      else:
        pair.append(elem)

    if level >= 4 and len(pair) == 2:
      return pair, False
    else:
      return None, False

  pair, _ = get_exploded_pair(number)

  if pair:
    str_number = json.dumps(number)
    index = str_number.index('"#"')
    left = ''
    right = ''
    first_i = False
    first_j = False
    i, j = index - 1, index + 3
    while i >= 0 or j < len(str_number):
      if i >= 0:
        char = str_number[i]
        if char.isnumeric() and not first_i:
          left = f'{char} + {pair[0]}' + left
          first_i = True
        else:
          left = char + left
        i -= 1
      if j < len(str_number):
        char = str_number[j]
        if char.isnumeric() and not first_j:
          right = right + f'{pair[1]} + {char}'
          first_j = True
        else:
          right = right + char
        j += 1
    return eval(left + '0' + right)
  else:
    return number

def reduce(number):
  previous_reduce_result = json.dumps(number)

  while True:
    number = explode(number)
    current_reduce_result = json.dumps(number)
    if previous_reduce_result == current_reduce_result:
      split(number)
      current_reduce_result = json.dumps(number)
      if previous_reduce_result == current_reduce_result:
        break
      else:
        previous_reduce_result = current_reduce_result
    else:
      previous_reduce_result = current_reduce_result

  return number

def calc_magnitude(number: List[Union[List, int]]) -> int:
  magnitude = 0

  for i, elem in enumerate(number):
    if isinstance(elem, list):
      magnitude += calc_magnitude(elem) * (3 - i)
    else:
      magnitude += elem * (3 - i)
  
  return magnitude

@process_puzzle_input(process_input)
def solve(input: List[str]) -> int:
  magnitudes = []

  for i in range(len(input)):
    for j in range(len(input)):
      if i != j:
        copy1 = copy.deepcopy(input[i])
        copy2 = copy.deepcopy(input[j])
        magnitudes.append(calc_magnitude(reduce([copy1, copy2])))

  return max(magnitudes)

if __name__ == '__main__':
  (Puzzle('Day 18 - Part 2', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 3993 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 4917 })
    .solve(solve))
