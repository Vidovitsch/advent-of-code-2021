import pathlib
from typing import Any, List
import numpy as np

from advent_helper.puzzle import Puzzle, PuzzleInput

def solve(bits: PuzzleInput) -> Any:
  a = process_packet(bits)
  return a[0]

def process_packet(bits):
  version = int(bits[:3], 2)
  type_id = int(bits[3:6], 2)

  if type_id == 4:
    value, length = calc_literal_value_and_length(bits)
    return value, length
  else:
    length_type_id = bits[6]
    if length_type_id == '0':
      total_length = 22
      values = []
      sub_packets_length = int(bits[7:7+15], 2)

      while total_length - 22 != sub_packets_length:
        value, length = process_packet(bits[total_length:])
        values.append(value)
        total_length += length
      
      return calc_value(values, type_id), total_length
    else:
      num_of_sub_packets = int(bits[7:7+11], 2)
      total_length = 18
      values = []
      for _ in range(num_of_sub_packets):
        value, length = process_packet(bits[total_length:])
        values.append(value)
        total_length += length

      return calc_value(values, type_id), total_length

def calc_value(values, type_id):
  if type_id == 0:
    return sum(values)
  elif type_id == 1:
    return np.prod(values)
  elif type_id == 2:
    return min(values)
  elif type_id == 3:
    return max(values)
  elif type_id == 5:
    return 1 if values[0] > values[1] else 0
  elif type_id == 6:
    return 1 if values[0] < values[1] else 0
  elif type_id == 7:
    return 1 if values[0] == values[1] else 0

def calc_literal_value_and_length(bits):
  literal_value = ''
  length = 6

  for i in range(6, len(bits), 5):
    group = bits[i:i + 5]
    literal_value += group[1:5]
    length += 5

    if group[0] == '0':
      break

  return int(literal_value, 2), length

def process_input(input: List[str]) -> PuzzleInput:
  hexadecimal_decoder = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
  }

  return''.join(hexadecimal_decoder[char] for char in input[0])

if __name__ == '__main__':
  (Puzzle('Day 16 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .set_input_processor(process_input)
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test5.txt', 'expected_result': 3 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test6.txt', 'expected_result': 54 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test7.txt', 'expected_result': 7 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test8.txt', 'expected_result': 9 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test9.txt', 'expected_result': 1 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test10.txt', 'expected_result': 0 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test11.txt', 'expected_result': 0 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test12.txt', 'expected_result': 1 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 258888628940 })
    .solve(solve))
