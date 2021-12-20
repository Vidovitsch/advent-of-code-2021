import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 8 - Part 2',
    CURRENT / 'input.txt',
    [
      {
        'input_path': CURRENT / 'test.txt',
        'expected_result': '61229'
      },
      {
        'input_path': CURRENT / 'input.txt',
        'expected_result': '1073431'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  return sum(get_output_value(*entry) for entry in get_entries(input))

def get_output_value(signal_patterns, encoded_output_value):
  signal_decoder = create_signal_decoder(signal_patterns)
  output_value = ''
  for number in encoded_output_value:
    output_value += str(signal_decoder[''.join(sorted(number))])
  return int(output_value)

def create_signal_decoder(signal_patterns):
  signal_decoder = [0] * 10

  for pattern in signal_patterns:
    pattern = ''.join(sorted(pattern))
    match len(pattern):
      case 2:
        signal_decoder[1] = pattern
      case 3:
       signal_decoder[7] = pattern
      case 4:
        signal_decoder[4] = pattern
      case 7:
        signal_decoder[8] = pattern

  for pattern in signal_patterns:
    pattern = ''.join(sorted(pattern))
    match len(pattern):
      case 5: # 2, 3, 5
        if len([char for char in signal_decoder[1] if char in pattern]) == 2:
          signal_decoder[3] = pattern
        elif len([char for char in signal_decoder[4] if char in pattern]) == 3:
          signal_decoder[5] = pattern
        else:
          signal_decoder[2] = pattern
      case 6: # 0, 6, 9
        if len([char for char in signal_decoder[4] if char in pattern]) == 4:
          signal_decoder[9] = pattern
        elif len([char for char in signal_decoder[1] if char in pattern]) == 2:
          signal_decoder[0] = pattern
        else:
          signal_decoder[6] = pattern
  return { pattern: i for i, pattern in enumerate(signal_decoder)}
  


def get_entries(input):
  entries = []

  for line in input:
    signal_patterns, output_value = line.split(' | ')
    entries.append([signal_patterns.split(), output_value.split()])

  return entries



if __name__ == '__main__':
  run()
