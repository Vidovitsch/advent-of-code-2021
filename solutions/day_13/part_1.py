import pathlib

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 13 - Part 1',
    CURRENT / 'input.txt',
    [
      {
        'input_path': CURRENT / 'test.txt',
        'expected_result': '17'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve, process_input)

##############################################################
# Solution
##############################################################

def process_input(line):
  if 'fold' in line:
    dimension, num = line.replace('fold along ', '').split('=')
    return [dimension, int(num)]

  return [int(num) for num in line.split(',')]

def solve(input):
  paper, folds = get_paper_and_folds(input)

  paper = fold_paper(paper, folds[0][0], folds[0][1])

  return len(paper)

def fold_paper(coordinates, fold_dimension, fold_index):
  dimension_index = 0 if fold_dimension == 'x' else 1

  for dot in coordinates:
    if dot[dimension_index] > fold_index:
      dot[dimension_index] = 2 * fold_index - dot[dimension_index]

  return set(map(tuple, coordinates))

def get_paper_and_folds(input):
  paper = []
  folds = []

  for line in input:
    if isinstance(line[0], int):
      paper.append(line)
    else:
      folds.append(line)

  return paper, folds

if __name__ == '__main__':
  run()
