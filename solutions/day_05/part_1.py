import pathlib
import numpy as np

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 5 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test.txt',
        'expected_result': '5'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '7674'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve)

##############################################################
# Solution
##############################################################

def solve(input):
  lines = [Line.from_coordinates_string(coordinates) for coordinates in input]
  max_x = max(max(line.x1, line.x2) for line in lines)
  max_y = max(max(line.y1, line.y2) for line in lines)
  
  canvas = np.zeros([max_y + 1, max_x + 1])
  for line in lines:
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
    if self.x1 == self.x2: # vertical
      min_y = min(self.y1, self.y2)
      max_y = max(self.y1, self.y2)
      for i in range(min_y, max_y + 1):
        canvas[i][self.x1] += 1
    elif self.y1 == self.y2: # horizontal
      min_x = min(self.x1, self.x2)
      max_x = max(self.x1, self.x2)
      for i in range(min_x, max_x + 1):
        canvas[self.y1][i] += 1

    return canvas

  def print(self):
    print(f'{self.x1},{self.y1} -> {self.x2},{self.y2}')

if __name__ == '__main__':
  run()
