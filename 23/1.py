import heapq
import pathlib
from typing import List, Tuple, Union

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

class Amphipod:
  def __init__(self, type: str, position: Tuple[int, int]) -> 'Amphipod':
    self.type = type
    self.position = position
  
  @property
  def hallway_position(self) -> int:
    return self.position[0]

  @property
  def side_room_position(self) -> int:
    return self.position[1]

  @property
  def required_energy(self) -> int:
    return {
      'A': 1,
      'B': 10,
      'C': 100,
      'D': 1000,
    }[self.type]

  @property
  def target_hallway_position(self) -> int:
    return {
      'A': 3,
      'B': 5,
      'C': 7,
      'D': 9,
    }[self.type]

  def is_in_a_side_room(self) -> bool:
    return self.position[1] > 0

  def is_in_position(self, related_amphipod: 'Amphipod') -> bool:
    if self.hallway_position != self.target_hallway_position: return False
    if self.side_room_position == 0: return False
    if self.side_room_position == 2: return True

    if self.side_room_position == 1:
      return related_amphipod.is_in_position(self)


class Burrow:
  AMPHIPODS = {
    'A': { 'energy': 1, 'target_room': 3 },
    'B': { 'energy': 10, 'target_room': 5 },
    'C': { 'energy': 100, 'target_room': 7 },
    'D': { 'energy': 1000, 'target_room': 9 }
  }
  TARGET_ROOMS = { value['target_room']: key for key, value in AMPHIPODS.items() }

  @classmethod
  def from_diagram(cls, diagram: List[str]) -> 'Burrow':
    amphipods = []

    for i in range(2, 4):
      for side_room in [amphipod['target_room'] for amphipod in cls.AMPHIPODS.values()]:
        amphipods.append(Amphipod(diagram[i][side_room], (side_room, i - 1)))

    return cls(amphipods)

  def __init__(self, amphipods: List['Amphipod'], energy_spent: int=0) -> 'Burrow':
    self.amphipods = amphipods
    self.energy_spent = energy_spent

  def is_organized(self) -> bool:
    for amphipod in self.amphipods:
      related_amphipod = [related for related in self.amphipods if related.type == amphipod.type and related != amphipod][0]
      if not amphipod.is_in_position(related_amphipod): return False
    
    return True

  def move(self) -> List['Burrow']:
    

  def manhattan(self):
    total_energy = 0

    tracked_amphipod_types = {}
    for amphipod in self.amphipods:
      related_amphipod = [related for related in self.amphipods if related.type == amphipod.type and related != amphipod][0]
      steps = 0
      if not amphipod.is_in_position(related_amphipod):
        steps = abs(amphipod.hallway_position - amphipod.target_hallway_position)

        if not amphipod.is_in_a_side_room():
          steps += 1 if amphipod.type in tracked_amphipod_types or related_amphipod.is_in_position(amphipod) else 2
        else:
          if amphipod.hallway_position == amphipod.target_hallway_position:
            steps += 0 if amphipod.type in tracked_amphipod_types or related_amphipod.is_in_position(amphipod) else 1
          else:
            steps += amphipod.side_room_position
            steps += 1 if amphipod.type in tracked_amphipod_types or related_amphipod.is_in_position(amphipod) else 2
        
      tracked_amphipod_types[amphipod.type] = 1
      total_energy += steps * amphipod.required_energy

    return total_energy

  def priority(self) -> int:
    return self.energy_spent + self.manhattan()

  def __lt__(self, other_burrow: 'Burrow') -> bool:
    return self.priority() < other_burrow.priority()

  def __str__(self) -> str:
    hallway = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    side_rooms = [['.', '.'], ['.', '.'], ['.', '.'], ['.', '.']]

    for amphipod in self.amphipods:
      if amphipod.side_room_position == 0:
        hallway[amphipod.hallway_position] = amphipod.type
      elif amphipod.hallway_position == 3:
        side_rooms[0][amphipod.side_room_position - 1] = amphipod.type
      elif amphipod.hallway_position == 5:
        side_rooms[1][amphipod.side_room_position - 1] = amphipod.type
      elif amphipod.hallway_position == 7:
        side_rooms[2][amphipod.side_room_position - 1] = amphipod.type
      elif amphipod.hallway_position == 9:
        side_rooms[3][amphipod.side_room_position - 1] = amphipod.type

    string = '#############'
    string += f"\n#{''.join(position for position in hallway)}#"
    string += f'\n###{side_rooms[0][0]}#{side_rooms[1][0]}#{side_rooms[2][0]}#{side_rooms[3][0]}###'
    string += f'\n###{side_rooms[0][1]}#{side_rooms[1][1]}#{side_rooms[2][1]}#{side_rooms[3][1]}###'
    string += '\n   #######   '

    return string

def process_input(input: List[str]) -> 'Burrow':
  return Burrow.from_diagram(input)

@process_puzzle_input(process_input)
def solve(burrow: 'Burrow') -> int:
  priority_queue = [burrow]
  print(burrow)
  
  heapq.heappush(priority_queue, Burrow(burrow.amphipods, 11))
  heapq.heappush(priority_queue, Burrow(burrow.amphipods, 222))
  heapq.heappush(priority_queue, Burrow(burrow.amphipods, 3))
  heapq.heappush(priority_queue, Burrow(burrow.amphipods, 1))

  while len(priority_queue) > 0:
    a = heapq.heappop(priority_queue)
    print(a.manhattan())

  return 0

if __name__ == '__main__':
  (Puzzle('Day 23: Amphipod - part 1', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 12521 })
    .solve(solve))
