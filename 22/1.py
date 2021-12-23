import pathlib
from typing import List, Tuple

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[Tuple[int, Tuple[Tuple[int, int]]]]

def process_input(input: List[str]) -> PuzzleInput:
  reboot_steps = []

  for line in input:
    power = 1 if line.split()[0] == 'on' else 0
    dimensions = tuple(tuple(map(int, dimension.split('=')[1].split('..'))) for dimension in line.split()[1].split(','))
    reboot_steps.append((power, dimensions))

  return reboot_steps

@process_puzzle_input(process_input)
def solve(reboot_steps: PuzzleInput) -> int:
  cubes = {}

  for power, dimensions in reboot_steps:
    set_cubes(power, dimensions, cubes)

  return len([power for power in cubes.values() if power])

def set_cubes(power, dimensions, cubes):
  x_range, y_range, z_range = dimensions

  if x_range[0] < -50 or x_range[1] > 50 or y_range[0] < -50 or y_range[1] > 50 or z_range[0] < -50 or z_range[1] > 50:
    return

  for x in range(x_range[0], x_range[1] + 1):
    for y in range(y_range[0], y_range[1] + 1):
      for z in range(z_range[0], z_range[1] + 1):
        cubes[(x, y, z)] = power

if __name__ == '__main__':
  (Puzzle('Day 22: Reactor Reboot - part 1', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 39 })
    .add_test({ 'input_path': CURRENT / 'test_2.txt', 'expected_result': 590784 })
    .solve(solve))
