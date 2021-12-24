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
    cuboid = Cuboid(*[tuple(map(int, dimension.split('=')[1].split('..'))) for dimension in line.split()[1].split(',')])
    reboot_steps.append((power, cuboid))

  return reboot_steps

@process_puzzle_input(process_input)
def solve(reboot_steps: PuzzleInput) -> int:
  
  for power, cuboids in reboot_steps:
    print(cuboids.x)

  return 0

class Cuboid:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  
  def cubes(self):
    return abs(self.x[0] - self.x[1]) * abs(self.y[0] - self.y[1]) * abs(self.z[0] - self.z[1])

  def overlapping_cubes(self, cuboid):
    return 0

if __name__ == '__main__':
  (Puzzle('Day 22: Reactor Reboot - part 2', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_3.txt', 'expected_result': 2758514936282235 })
    .solve(solve))
