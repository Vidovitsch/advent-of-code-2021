import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 11 - Part 2',
    CURRENT / 'input.txt',
    [
      {
        'input_path': CURRENT / 'test.txt',
        'expected_result': '195'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve, process_input)

##############################################################
# Solution
##############################################################

def process_input(line):
  return [int(char) for char in line]

def solve(energy_level_map):
  flash_count = 0

  i = 1
  while True:
    add_1(energy_level_map)
    if calculate_flash_count(energy_level_map) == len(energy_level_map) * len(energy_level_map[0]):
      break
    i += 1

  return i

def calculate_flash_count(energy_level_map):
  flash_count = 0

  for row in range(len(energy_level_map)):
    for col in range(len(energy_level_map[0])):
      if energy_level_map[row][col] > 9:
        flash_count += flash(row, col, energy_level_map)

  return flash_count

def flash(row, col, energy_level_map):
  if 0 <= row < len(energy_level_map) and 0 <= col < len(energy_level_map[0]):
    energy_level = energy_level_map[row][col]

    if energy_level == 0:
      return 0
    if energy_level <= 9:
      energy_level_map[row][col] += 1

    if energy_level_map[row][col] > 9:
      energy_level_map[row][col] = 0
      adjacents = [
        flash(row + 1, col, energy_level_map), # top
        flash(row - 1, col, energy_level_map), # bottom
        flash(row, col + 1, energy_level_map), # right
        flash(row, col - 1, energy_level_map), # left
        flash(row + 1, col + 1, energy_level_map), # top-right
        flash(row + 1, col - 1, energy_level_map), # top-left
        flash(row - 1, col + 1, energy_level_map), # bottom-right
        flash(row - 1, col - 1, energy_level_map) # bottom-left
      ]
      return sum(adjacents) + 1
    return 0
  else:
    return 0
    
def add_1(energy_level_map):
  for row in range(len(energy_level_map)):
    for col in range(len(energy_level_map[0])):
      energy_level_map[row][col] += 1

if __name__ == '__main__':
  run()
