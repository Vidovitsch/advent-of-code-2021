import math
import pathlib
from typing import Any, List

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

def process_input(input: List[str]) -> List[Any]:
  scanners = []

  for line in input:
    if 'scanner' in line:
      base_scanner = scanners[0] if len(scanners) > 0 else None
      scanners.append(Scanner(line, base_scanner))
    elif len(scanners) > 0:
      scanners[-1].beacons.append(tuple(map(int, line.split(','))))

  return scanners

def common_elements(list_1, list_2):
  common = []

  def index(value, list):
    try:
      return list.index(value)
    except ValueError:
      return None

  copy = [elem for elem in list_2]
  for element_1 in list_1:
    i = index(element_1, copy)
    if i is not None:
      common.append(element_1)
      del copy[i]
  
  return common

class Scanner:
  def __init__(self, name: str, base_scanner: 'Scanner'=None):
    self.name = name
    self.base_scanner = base_scanner
    self.beacons = []
    self.absolute_position = (None, None, None) if base_scanner else (0, 0, 0)
    self.absolute_beacons = [] if base_scanner else self.beacons

  def beacon_distances(self):
    distances = [[float(0)] * len(self.beacons) for _ in range(len(self.beacons))]

    for i, beacon_1 in enumerate(self.beacons):
      for j, beacon_2 in enumerate(self.beacons):
        if i == j: continue
        distances[i][j] = math.sqrt(sum((beacon_1[k] - beacon_2[k]) ** 2 for k in range(len(beacon_1))))

    return distances
  
  def overlapping_beacons(self, scanner: 'Scanner'):
    distances_1 = self.beacon_distances()
    distances_2 = scanner.beacon_distances()

    overlapping_beacons = []

    for i in range(len(distances_1)):
      for j in range(len(distances_2)):
        common = common_elements(distances_1[i], distances_2[j])
        if len(common) >= 12:
          overlapping_beacons.append((self.beacons[i], scanner.beacons[j]))

    if len(overlapping_beacons) >= 12:
      return overlapping_beacons
  
  def set_absolute_position(self, overlapping_beacons):
    orientations = [
      (0, 1, 2),
      (0, 2, 1),
      (1, 0, 2),
      (1, 2, 0),
      (2, 0, 1),
      (2, 1, 0),
    ]
    signs = [
      (1, 1, 1),
      (1, -1, 1),
      (1, 1, -1),
      (1, -1, -1),
      (-1, 1, 1),
      (-1, -1, 1),
      (-1, 1, -1),
      (-1, -1, -1),
    ]
    for orientation in orientations:
      for sign in signs:
        diffs = []
        for aligned, a in overlapping_beacons:
          b = (a[orientation[0]] * sign[0], a[orientation[1]] * sign[1], a[orientation[2]] * sign[2])
          diff = (aligned[0] - b[0], aligned[1] - b[1], aligned[2] - b[2])
          diffs.append(diff)
        if len(set(diffs)) == 1:
          self.absolute_position = diffs[0]
          for b in self.beacons:
            ab = (b[orientation[0]] * sign[0] + diffs[0][0], b[orientation[1]] * sign[1] + diffs[0][1], b[orientation[2]] * sign[2] + diffs[0][2])
            self.absolute_beacons.append(ab)
          self.beacons = self.absolute_beacons
          return self.absolute_position

    return None

@process_puzzle_input(process_input)
def solve(scanners: List[Scanner]) -> int:
  absolute_scanners = [scanners[0]]

  count = 0
  while len(absolute_scanners) != len(scanners):
    abs_scanner = absolute_scanners[count]
    for rel_scanner in scanners:
      if abs_scanner == rel_scanner or rel_scanner in absolute_scanners:
        continue

      overlaps = abs_scanner.overlapping_beacons(rel_scanner)
      if overlaps:
        rel_scanner.set_absolute_position(overlaps)
        absolute_scanners.append(rel_scanner)
    count += 1

  beacons = []
  for s in absolute_scanners:
    for b in s.absolute_beacons:
      beacons.append(b)
  
  return len(set(beacons))

if __name__ == '__main__':
  (Puzzle('Day 19 - Part 1', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 79 })
    .solve(solve))
