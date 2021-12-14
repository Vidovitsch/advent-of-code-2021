import pathlib
from collections import Counter

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 14 - Part 2',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '2188189693529'
      }
    ]
  )

def run():
  get_puzzle().run_tests_with(solve, process_input)

##############################################################
# Solution
##############################################################

def process_input(line):
  if '->' in line:
    return line.split(' -> ')

  return line

def solve(input):
  template, rules = input[0], { pair: insertion for pair, insertion in input[1:] }
  
  for _ in range(20):
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
