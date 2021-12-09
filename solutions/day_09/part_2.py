import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 9 - Part 2',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '1134'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  input = get_input(input)
  total_basin_size = 1
  basin_sizes = []
  for y in range(len(input)):
    for x in range(len(input[0])):
      if int(input[y][x]) != 9:
        basin_sizes.append(get_basin_size(x, y, input))
  basin_sizes = sorted(basin_sizes, reverse=True)

  return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

def get_basin_size(x, y, heightmap):
  if int(heightmap[y][x]) == 9:
    return 0

  heightmap[y][x] = 9

  adjacents = [
    get_basin_size(x - 1, y, heightmap) if x > 0 else 0,
    get_basin_size(x + 1, y, heightmap) if x < len(heightmap[0]) - 1 else 0,
    get_basin_size(x, y - 1, heightmap) if y > 0 else 0,
    get_basin_size(x, y + 1, heightmap) if y < len(heightmap) - 1 else 0
  ]

  return sum(adjacents) + 1

def get_input(input):
  processed_input = []
  for row in input:
    processed_input.append([int(char) for char in row])
  return processed_input

if __name__ == '__main__':
  run()
