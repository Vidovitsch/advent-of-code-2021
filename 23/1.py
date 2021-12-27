import pathlib
from typing import List, Tuple, Union

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

class Burrow:
  AMPHIPOD_ENCODINGS = { 'A': 3, 'B': 5, 'C': 7, 'D': 9 }
  AMPHIPOD_DECODINGS = { value: key for key, value in AMPHIPOD_ENCODINGS.items() }

  @classmethod
  def from_diagram(cls, diagram: List[str]) -> 'Burrow':
    state = [0] * 11

    for i in range(2, 4):
      for side_room in cls.AMPHIPOD_ENCODINGS.values():
        if not state[side_room]:
          state[side_room] = [0] * 3
        state[side_room][i - 1] = cls.AMPHIPOD_ENCODINGS[diagram[i][side_room]]

    return cls(state)

  def __init__(self, state: List[Union[int, List[int]]]) -> 'Burrow':
    self.state = state

  def show(self):
    print('#############')
    print(f"#{''.join(self.AMPHIPOD_DECODINGS[i] if i in self.AMPHIPOD_DECODINGS else '.' for i in self._hallway_state())}#")
    print(f'###{self.AMPHIPOD_DECODINGS[self.state[3][1]]}#{self.AMPHIPOD_DECODINGS[self.state[5][1]]}#{self.AMPHIPOD_DECODINGS[self.state[7][1]]}#{self.AMPHIPOD_DECODINGS[self.state[9][1]]}###')
    print(f'###{self.AMPHIPOD_DECODINGS[self.state[3][2]]}#{self.AMPHIPOD_DECODINGS[self.state[5][2]]}#{self.AMPHIPOD_DECODINGS[self.state[7][2]]}#{self.AMPHIPOD_DECODINGS[self.state[9][2]]}###')
    print('   #######   ')

  def _hallway_state(self) -> List[int]:
    hallway_state = []

    for elem in self.state:
      if isinstance(elem, list):
        hallway_state.append(elem[0])
      else:
        hallway_state.append(elem)
    
    return hallway_state

def process_input(input: List[str]) -> Burrow:
  return Burrow.from_diagram(input)

@process_puzzle_input(process_input)
def solve(burrow: Burrow) -> int:
  print()
  burrow.show()
  return 0

if __name__ == '__main__':
  (Puzzle('Day 23: Amphipod - part 1', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 12521 })
    .solve(solve))
