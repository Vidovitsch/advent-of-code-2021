import pathlib
from typing import Any, List

import numpy as np

from advent_helper.puzzle import Puzzle, PuzzleInput

def solve(input: PuzzleInput) -> Any:
  max_x = max(max(line.x1, line.x2) for line in input)
  max_y = max(max(line.y1, line.y2) for line in input)
  
  canvas = np.zeros([max_y + 1, max_x + 1])
  for line in input:
    line.write_on_canvas(canvas)
  
  return (canvas > 1).sum()

class Line:
  @classmethod
  def from_coordinates_string(cls, coordinates):
    return cls(*[coordinates.split(',') for coordinates in coordinates.split(' -> ')])
    
  def __init__(self, start, end):
    self.x1 = int(start[0])
    self.y1 = int(start[1])
    self.x2 = int(end[0])
    self.y2 = int(end[1])

  def write_on_canvas(self, canvas):
    min_x = min(self.x1, self.x2)
    max_x = max(self.x1, self.x2)
    min_y = min(self.y1, self.y2)
    max_y = max(self.y1, self.y2)
    if self.x1 == self.x2: # vertical
      for i in range(min_y, max_y + 1):
        canvas[i][self.x1] += 1
    elif self.y1 == self.y2: # horizontal
      for i in range(min_x, max_x + 1):
        canvas[self.y1][i] += 1
    else: # diagonal (45 degrees)
      x = self.x1
      y = self.y1
      canvas[y][x] += 1
      for i in range(abs(self.x1 - self.x2)):
        if x < self.x2:
          x += 1
        else:
          x -= 1
        if y < self.y2:
          y += 1
        else:
          y -= 1
        canvas[y][x] += 1

    return canvas

def process_input(input: List[str]) -> PuzzleInput:
  return [Line.from_coordinates_string(coordinates) for coordinates in input]

if __name__ == '__main__':
  (Puzzle('Day 5 - Part 2', pathlib.Path(__file__).parent / 'input.txt')
    .set_input_processor(process_input)
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 12 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 20898 })
    .solve(solve))
