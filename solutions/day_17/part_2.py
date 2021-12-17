import pathlib
from typing import List, Tuple

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

def process_input(input: List[str]) -> Tuple[int, int, int, int]:
  target_area = []

  for dimension in input[0][13:].split(', '):
    target_area += sorted(map(int, dimension[2:].split('..')))
  
  return target_area

@process_puzzle_input(process_input)
def solve(target_area: Tuple[int, int, int, int]) -> int:
  x_values = calc_possible_x_velocities(target_area)
  y_values = calc_possible_y_velocities(target_area)

  count = 0
  for x in x_values:
    for y in y_values:
      value = shoot_probe((x, y), target_area)
      if value is not None:
        count += 1
  return count

def calc_possible_y_velocities(target_area: Tuple[int, int, int, int]) -> List[int]:
  area_x1, area_x2, area_y1, area_y2 = target_area

  values = []
  for i in range(area_y1, abs(area_y1)):
    m = shoot_probe((0, i), target_area, drag=0, gravity=1, x=area_x1, y=0)
    if m is not None:
      values.append(i)
  return values

def calc_possible_x_velocities(target_area: Tuple[int, int, int, int]) -> List[int]:
  area_x1, area_x2, area_y1, area_y2 = target_area

  values = []
  if 0 < area_x1:
    for i in range(area_x2 + 1):
      m = shoot_probe((i, 0), target_area, drag=1, gravity=0, x=0, y=area_y1)
      if m is not None:
        values.append(i)

  return values

def shoot_probe(velocity: Tuple[int, int], target_area: Tuple[int, int, int, int], drag=1, gravity=1, x=0, y=0) -> int:
  vel_x, vel_y = velocity
  x = x
  y = y

  max_y = 0
  while not will_never_hit((vel_x, vel_y), (x, y), target_area):
    if y > max_y:
      max_y = y

    if in_taget_area((x, y), target_area):
      return max_y

    x += vel_x
    y += vel_y

    if vel_x > 0:
      vel_x -= drag
    elif vel_x < 0:
      vel_x += drag
   
    vel_y -= gravity
    
  return None

def in_taget_area(location: Tuple[int, int], target_area: Tuple[int, int, int, int]) -> bool:
  x, y = location

  area_x1, area_x2, area_y1, area_y2 = target_area

  return area_x1 <= x <= area_x2 and area_y1 <= y <= area_y2

def will_never_hit(velocity: Tuple[int, int], location: Tuple[int, int], target_area: Tuple[int, int, int, int]) -> bool:
  x, y = location
  area_x1, area_x2, area_y1, area_y2 = target_area
  
  if y < area_y1:
    return True
  elif x > area_x2 and velocity[0] >= 0:
    return True
  elif x < area_x1 and velocity[0] <= 0:
    return True
  else:
    return False

if __name__ == '__main__':
  (Puzzle('Day 17 - Part 2', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 112 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 4716 })
    .solve(solve))
