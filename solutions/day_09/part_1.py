import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 9 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '15'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '524'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  total_risk_level = 0
  for y in range(len(input)):
    for x in range(len(input[0])):
      total_risk_level += risk_level(x, y, input)
  return total_risk_level

def risk_level(x, y, heightmap):
  height = int(heightmap[y][x])

  adjecent_heights = [
    int(heightmap[y][x - 1]) if x > 0 else None,
    int(heightmap[y][x + 1]) if x < len(heightmap[0]) - 1 else None,
    int(heightmap[y - 1][x]) if y > 0 else None,
    int(heightmap[y + 1][x]) if y < len(heightmap) - 1 else None
  ]

  min_adjecent_height = min(height for height in adjecent_heights if height is not None)
  
  return height + 1 if min_adjecent_height > height else 0


if __name__ == '__main__':
  run()
