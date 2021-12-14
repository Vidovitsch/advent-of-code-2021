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
  get_puzzle().solve_with(solve, process_input)

##############################################################
# Solution
##############################################################

def process_input(line):
  if '->' in line:
    return line.split(' -> ')

  return line

def solve(input):
  steps = 40
  template, rules = input[0], { pair: insertion for pair, insertion in input[1:] }
  rule_step_counter = create_rule_step_counter(rules, int(steps / 2))

  for _ in range(int(steps / 2)):
    template = step(template, rules)
  
  counter = Counter({})
  for i in range(len(template) - 1):
    pair = template[i:i + 2]
    counter += Counter(rule_step_counter[pair])
  
  counter[template[-1]] += 1

  return max(counter.values()) - min(counter.values())

def create_rule_step_counter(rules, steps):
  def next_step(pair, counter, step=1):
    char = rules[pair]
    counter[char] += 1

    if step == steps:
      return

    next_step(pair[0] + char, counter, step + 1)
    next_step(char + pair[1], counter, step + 1)

  rule_step_counter = {}

  for pair in rules.keys():
    if pair not in rule_step_counter:
      rule_step_counter[pair] = 0
    counter = { char: 0 for char in rules.values() }
    next_step(pair, counter)
    counter[pair[0]] += 1
    rule_step_counter[pair] = counter

  return rule_step_counter

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
