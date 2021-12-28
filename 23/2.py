import dataclasses
import heapq
import pathlib
import typing 

import numpy as np

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

A, B, C, D = 10 ** np.arange(4)

ROOM_DOORS = {
    A: 2,
    B: 4,
    C: 6,
    D: 8,
}

ROOMS = {
    A: 0,
    B: 1,
    C: 2,
    D: 3,
}


@dataclasses.dataclass(frozen=True)
class Room:
    type: int
    size: int
    amphipods: tuple[int]

    def is_final(self):
        return len(self.amphipods) == self.size and all(amphipod == self.type for amphipod in self.amphipods)

    def is_enterable(self):
        return len(self.amphipods) < self.size and all(amphipod == self.type for amphipod in self.amphipods)

    def __len__(self):
        return len(self.amphipods)

    def pop(self):
        if not self.amphipods:
            raise ValueError('Room is empty')

        return self.amphipods[-1], dataclasses.replace(self, amphipods=self.amphipods[:-1])

    def append(self, amphipod):
        return dataclasses.replace(self, amphipods=self.amphipods + (amphipod,))

    def gap(self):
        return self.size - len(self.amphipods)


@dataclasses.dataclass(frozen=True)
class Hallway:
    spaces: tuple[typing.Optional[int]] = (None,) * 11
    DOORS: typing.ClassVar = set(ROOM_DOORS.values())

    def __iter__(self):
        return iter(self.spaces)

    def get_valid_moves(self, start):
        left_range = range(start - 1, -1, -1)
        right_range = range(start + 1, 11, 1)

        for search_range in [left_range, right_range]:
            for space in search_range:
                if space in self.DOORS:
                    continue

                if self.spaces[space] is not None:
                    break

                distance = abs(start - space)
                yield (space, distance)

    def is_clear(self, start, stop):
        if start < stop:
            search_range = range(start + 1, stop + 1)
        else:
            search_range = range(stop, start)

        return all(self.spaces[space] is None for space in search_range)

    def update_space(self, space, amphipod):
        return Hallway(self.spaces[:space] + (amphipod,) + self.spaces[space + 1:])


@dataclasses.dataclass(frozen=True)
class State:
    energy: int
    rooms: tuple[Room]
    hallway: Hallway

    def __hash__(self):
        return hash((self.rooms, self.hallway))

    def __eq__(self, other):
        return isinstance(other, State) and hash(self) == hash(other)

    def __lt__(self, other):
        return self.energy < other.energy

    def is_final(self):
        return all(room.is_final() for room in self.rooms)

    def update_room(self, i, new_room):
        return self.rooms[:i] + (new_room,) + self.rooms[i + 1:]


def get_best_path(initial_state):
    heap = [initial_state]
    visited = set()

    while heap:
        state = heapq.heappop(heap)
        if state.is_final():
            return state.energy
        if state in visited:
            continue

        visited.add(state)

        # Generate all next states where an amphipod moves into a hallway
        for i, room in enumerate(state.rooms):
            if room and not room.is_final():
                amphipod, new_room = room.pop()
                door = ROOM_DOORS[room.type]

                for space, distance in state.hallway.get_valid_moves(door):
                    new_state = State(
                        state.energy + (room.gap() + 1 + distance) * amphipod,
                        state.update_room(i, new_room),
                        state.hallway.update_space(space, amphipod),
                    )
                    if new_state not in visited:
                        heapq.heappush(heap, new_state)

        # Generate all next states where an amphipod moves into a room
        for space, amphipod in enumerate(state.hallway):
            if amphipod is None:
                continue

            door = ROOM_DOORS[amphipod]
            room_idx = ROOMS[amphipod]
            room = state.rooms[room_idx]

            if state.hallway.is_clear(space, door) and room.is_enterable():
                new_room = room.append(amphipod)
                distance = abs(door - space)

                new_state = State(
                    state.energy + (distance + room.gap()) * amphipod,
                    state.update_room(room_idx, new_room),
                    state.hallway.update_space(space, None),
                )
                if new_state not in visited:
                    heapq.heappush(heap, new_state)

def solve(input: typing.List[str]):
    rooms = { 0: [], 1: [], 2: [], 3: [] }

    for i in range(2, len(input) - 1):
      for j, k in enumerate((3, 5, 7, 9)):
        type = input[i][k]
        match type:
          case 'A':
            rooms[j].append(A)
          case 'B':
            rooms[j].append(B)
          case 'C':
            rooms[j].append(C)
          case 'D':
            rooms[j].append(D)

      if i == 2:
        rooms[0].append(D)
        rooms[0].append(D)
        rooms[1].append(C)
        rooms[1].append(B)
        rooms[2].append(B)
        rooms[2].append(A)
        rooms[3].append(A)
        rooms[3].append(C)
    
    return get_best_path(State(
        0,
        (
            Room(A, len(rooms[0]), tuple(reversed(rooms[0]))),
            Room(B, len(rooms[1]), tuple(reversed(rooms[1]))),
            Room(C, len(rooms[2]), tuple(reversed(rooms[2]))),
            Room(D, len(rooms[3]), tuple(reversed(rooms[3]))),
        ),
        Hallway(),
    ))

if __name__ == '__main__':
  (Puzzle('Day 23: Amphipod - part 2', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 44169 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 49936 })
    .solve(solve))
