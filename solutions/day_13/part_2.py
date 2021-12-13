import pathlib

from advent_helper import puzzle
import numpy as np

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 13 - Part 2',
    pathlib.Path(__file__).parent / 'input.txt'
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

  for fold in folds:
    paper = fold_paper(paper, fold[0], fold[1])

  print_paper(paper)

def fold_paper(coordinates, fold_dimension, fold_index):
  dimension_index = 0 if fold_dimension == 'x' else 1

  for dot in coordinates:
    if dot[dimension_index] > fold_index:
      dot[dimension_index] = 2 * fold_index - dot[dimension_index]

  return [list(coordinate) for coordinate in set(map(tuple, coordinates))]

def print_paper(coordinates):
  rows = max(coordinate[1] for coordinate in coordinates) + 1
  cols = max(coordinate[0] for coordinate in coordinates) + 1
  grid = [[' ' for _ in range(cols)] for _ in range(rows)]

  for dot in coordinates:
    grid[dot[1]][dot[0]] = '#'
  
  for row in grid:
    for i in row:
      print(i, end='')
    print()

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
