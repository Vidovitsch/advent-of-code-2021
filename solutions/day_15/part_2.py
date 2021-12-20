import pathlib
from typing import Any, List
from collections import namedtuple, deque
import sys
from advent_helper.puzzle import Puzzle, PuzzleInput
import heapq

def dijkstra(grid, target, start=(0, 0), risk=0):
  queue = [(risk, start)]
  minRisk = {start: risk}
  visited = {start}

  while queue:
    risk, (x, y) = heapq.heappop(queue)
    if (x, y) == target: return risk

    for neighb in ((x+1, y), (x, y+1), (x-1, y), (x, y-1)):
      if neighb not in grid or neighb in visited: continue
      visited.add(neighb)
      newRisk = risk + grid[neighb]
      if newRisk < minRisk.get(neighb, 999999):
        minRisk[neighb] = newRisk
        heapq.heappush(queue, (newRisk, neighb))

def solve(input: PuzzleInput) -> Any:
  maxX, maxY = map(max, zip(*input))

  return dijkstra(input, (maxX, maxY))

def process_input(input: List[str]) -> PuzzleInput:
  processed_input = {}

  for y, row in enumerate(input):
    for x, n in enumerate(row):
      for tile_y in range(5):
        for tile_x in range(5):
          processed_input[(x + tile_x * len(row), y + tile_y * len(input))] = (int(n) + tile_y + tile_x) % 9 or 9

  return processed_input

if __name__ == '__main__':
  (Puzzle('Day 15 - Part 2', CURRENT / 'input.txt')
    .set_input_processor(process_input)
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 315 })
    .solve(solve))
