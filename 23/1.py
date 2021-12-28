import heapq
import pathlib
from typing import List, Tuple, Union

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

class Amphipod:
  AMPHIPODS = {
    'A': { 'energy': 1, 'target_room': 2 },
    'B': { 'energy': 10, 'target_room': 4 },
    'C': { 'energy': 100, 'target_room': 6 },
    'D': { 'energy': 1000, 'target_room': 8 }
  }

  def __init__(self, type: str, pos: Tuple[int, int]) -> 'Amphipod':
    self.type = type
    self.pos = pos
    self.energy = self.AMPHIPODS[type]['energy']
    self.target_pos = ((self.AMPHIPODS[type]['target_room'], 1), (self.AMPHIPODS[type]['target_room'], 2))

  def __str__(self) -> str:
    return self.type

class Burrow:
  @classmethod
  def from_diagram(cls, diagram: List[str]) -> 'Burrow':
    amphipods = { 'A': [], 'B': [], 'C': [], 'D': [] }
    grid = [['.'], ['.'], ['.', '.', '.'], ['.'], ['.', '.', '.'], ['.'], ['.', '.', '.'], ['.'], ['.', '.', '.'], ['.'], ['.']]
    target_rooms = (2, 4, 6, 8)

    for room_pos in range(2, 4):
      for room in target_rooms:
        type = diagram[room_pos][room + 1]
        amphipod = Amphipod(type, (room, room_pos - 1))
        grid[room][room_pos - 1] = amphipod
        amphipods[type].append(amphipod)

    return cls(grid, amphipods)

  def __init__(self, grid: List[List[Union[str, object]]], amphipods: List['Amphipod'], energy_spent: int=0) -> 'Burrow':
    self.grid = grid
    self.amphipods = amphipods
    self.energy_spent = energy_spent

  def hallway(self) -> List[Union[str, object]]:
    return [pos[0] for pos in self.grid]

  def room(self, number: int) -> List[Union[str, object]]:
    if number in (2, 4, 6, 8): return self.grid[number][1:]

  def is_organized(self) -> bool:
    return self.manhattan() == 0

  def move(self) -> List['Burrow']:
    return None

  def manhattan(self):
    total_energy = 0

    for related_amphipods in self.amphipods.values():
      for i, amphipod in enumerate(related_amphipods):
        total_energy += self._amphipod_manhattan(amphipod) - i * amphipod.energy

    return total_energy

  def priority(self) -> int:
    return self.energy_spent + self.manhattan()

  def _amphipod_in_position(self, amphipod: 'Amphipod') -> bool:
    related_amphipod = self._related_amphipod(amphipod)

    if amphipod.pos in amphipod.target_pos:
      if amphipod.pos[1] == 2:
        return True
      elif related_amphipod.pos in related_amphipod.target_pos and related_amphipod.pos[1] == 2:
        return True
    
    return False
  
  def _amphipod_manhattan(self, amphipod: 'Amphipod') -> int:
    if amphipod.pos == amphipod.target_pos[1]: return 0
    
    steps = abs(amphipod.pos[0] - amphipod.target_pos[0][0]) # hallway steps
    if amphipod.pos[1] > 0:
      if amphipod.pos[0] == amphipod.target_pos[0][0]:
        steps += 1 # steps to end of target room (when in target room already)
      else:
        steps += amphipod.pos[1] + 2 # steps out of current room + steps to end of target room
    else:
      steps += 2 # steps to end of target room

    return steps * amphipod.energy

  def _related_amphipod(self, amphipod: 'Amphipod') -> 'Amphipod':
    return [related_amphipod for related_amphipod in self.amphipods[amphipod.type] if related_amphipod is not amphipod]


  def __lt__(self, burrow: 'Burrow') -> bool:
    return self.priority() < burrow.priority()

  def __str__(self) -> str:
    string = '#############'
    string += f"\n#{''.join(self.hallway())}#"
    string += f'\n###{self.room(2)[0]}#{self.room(4)[0]}#{self.room(6)[0]}#{self.room(8)[0]}###'
    string += f'\n###{self.room(2)[1]}#{self.room(4)[1]}#{self.room(6)[1]}#{self.room(8)[1]}###'

    return string + '\n   #######   '

def process_input(input: List[str]) -> 'Burrow':
  return Burrow.from_diagram(input)

@process_puzzle_input(process_input)
def solve(burrow: 'Burrow') -> int:
  priority_queue = [burrow]
  print()
  print(burrow)
  print(burrow.manhattan())
  
  heapq.heappush(priority_queue, Burrow(burrow.grid, burrow.amphipods))
  heapq.heappush(priority_queue, Burrow(burrow.grid, burrow.amphipods))
  heapq.heappush(priority_queue, Burrow(burrow.grid, burrow.amphipods, 222))
  heapq.heappush(priority_queue, Burrow(burrow.grid, burrow.amphipods, 22))

  while len(priority_queue) > 0:
    a = heapq.heappop(priority_queue)
    print(a.priority())

  return 0

if __name__ == '__main__':
  (Puzzle('Day 23: Amphipod - part 1', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 12521 })
    .solve(solve))
