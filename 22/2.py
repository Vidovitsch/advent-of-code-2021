import pathlib
from typing import Any, List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[Any]

def process_input(input: List[str]) -> PuzzleInput:
  reboot_steps = []

  for line in input:
    powered = 1 if line.split()[0] == 'on' else 0
    cuboid = Cuboid(*[tuple(map(int, dimension.split('=')[1].split('..'))) for dimension in line.split()[1].split(',')], powered)
    reboot_steps.append(cuboid)

  return reboot_steps

@process_puzzle_input(process_input)
def solve(cuboids: PuzzleInput) -> int:
  cuboids = list(reversed(cuboids))
  total_power = [0, 0] # [off, on]

  for i, cuboid in enumerate(cuboids):
    power = [0, 0]
    power[cuboid.powered] = cuboid.cubes()

    power[cuboid.powered] -= cuboid.overlapping_cubes(cuboids[:i])

    total_power[0] += power[0]
    total_power[1] += power[1]

  return total_power[1]

def remove_inner_overlap(cuboids: List[Any]):
  inner_overlapping_cuboids = []

  for i, cuboid_1 in enumerate(cuboids):
    for cuboid_2 in cuboids[i + 1:]:
      if overlap := cuboid_1.overlap(cuboid_2):
        if overlap.fingerprint() == cuboid_1.fingerprint():
          inner_overlapping_cuboids.append(cuboid_1)
        elif overlap.fingerprint() == cuboid_2.fingerprint():
          inner_overlapping_cuboids.append(cuboid_2)

  return [cuboid for cuboid in cuboids if cuboid not in inner_overlapping_cuboids]


class Cuboid:
  def __init__(self, x, y, z, powered):
    self.x = x
    self.y = y
    self.z = z
    self.powered = powered
  
  def cubes(self):
    return (abs(self.x[0] - self.x[1]) + 1) * (abs(self.y[0] - self.y[1]) + 1) * (abs(self.z[0] - self.z[1]) + 1)

  def overlap(self, cuboid: 'Cuboid'):
    if not self._does_overlap(cuboid): return

    return Cuboid(
      (max(self.x[0], cuboid.x[0]), min(self.x[1], cuboid.x[1])),
      (max(self.y[0], cuboid.y[0]), min(self.y[1], cuboid.y[1])),
      (max(self.z[0], cuboid.z[0]), min(self.z[1], cuboid.z[1])),
      self.powered
    )

  def overlapping_cubes(self, cuboids: List['Cuboid']):
    overlapping_cuboids = []
    for cuboid in cuboids:
      if overlap := self.overlap(cuboid):
        overlapping_cuboids.append(overlap)

    overlapping_cuboids = remove_inner_overlap(overlapping_cuboids)

    def count_overlapping_cubes(cuboids):
      seen_cuboids = []
      total_sum = 0
      for cuboid in cuboids:
        overlapping_cuboids = []

        for seen_cuboid in seen_cuboids:
          if overlap := cuboid.overlap(seen_cuboid):
            overlapping_cuboids.append(overlap)

        total_sum += cuboid.cubes()
        total_sum -= count_overlapping_cubes(overlapping_cuboids)
        seen_cuboids.append(cuboid)
      return total_sum
    
    return count_overlapping_cubes(overlapping_cuboids)

  def _does_overlap(self, cuboid: 'Cuboid'):
    if max(self.x) < min(cuboid.x): return False
    if min(self.x) > max(cuboid.x): return False
    if max(self.y) < min(cuboid.y): return False
    if min(self.y) > max(cuboid.y): return False
    if max(self.z) < min(cuboid.z): return False
    if min(self.z) > max(cuboid.z): return False

    return True

  def fingerprint(self):
    return (self.x, self.y, self.z, self.powered)

  def show(self):
    print(f"x={min(self.x)}..{max(self.x)} y={min(self.y)}..{max(self.y)} z={min(self.z)}..{max(self.z)} [cubes={self.cubes()}, power={'on' if self.powered else 'off'}]")

if __name__ == '__main__':
  (Puzzle('Day 22: Reactor Reboot - part 2', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test_1.txt', 'expected_result': 39 })
    .add_test({ 'input_path': CURRENT / 'test_4.txt', 'expected_result': 590784 })
    .add_test({ 'input_path': CURRENT / 'test_3.txt', 'expected_result': 2758514936282235 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 1235484513229032 })
    .solve(solve))
