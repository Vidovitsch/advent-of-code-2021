import pathlib
from collections import Counter

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 14 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '1588'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '2874'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve, process_input)

##############################################################
# Solution
##############################################################

def process_input(lines):
  processed_input = []

  for line in lines:
    if '->' in line:
      processed_input.append(line.split(' -> '))
    else:
      processed_input.append(line)
  
  return processed_input

def solve(input):
  template, rules = input[0], { pair: insertion for pair, insertion in input[1:] }
  
  for _ in range(10):
    template = step(template, rules)

  counts = Counter(template).values()

  return max(counts) - min(counts)

def step(template, rules):
  new_template = template[0]

  i = 0
  while i < len(template) - 1:
    pair = template[i:i + 2]

    if pair in rules:
      new_template += rules[pair]
    new_template += pair[1]

    i += 1
  
  return new_template

if __name__ == '__main__':
  run()
