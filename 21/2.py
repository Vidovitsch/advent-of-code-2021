from itertools import product
import pathlib
from typing import List, Tuple

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

CURRENT = pathlib.Path(__file__).parent

PuzzleInput = List[Tuple[int, int]]

def process_input(input: List[str]) -> PuzzleInput:
  return [(int(line.split(': ')[1]), 0) for line in input]

@process_puzzle_input(process_input)
def solve(players: PuzzleInput) -> int:
  return max(play(players[0], players[1], get_roll_combinations(3)))

def play(player_1, player_2, roll_combinations, game_states={}):
  def next_turn(player_1, player_2, player_1_turn=True):
    game_state = (player_1, player_2, player_1_turn)
    if game_state in game_states: return game_states[game_state]
    if player_1[1] >= 21: return [1, 0]
    if player_2[1] >= 21: return [0, 1]

    position, score = player_1 if player_1_turn else player_2

    total_won = [0, 0]
    for roll in roll_combinations:
      new_position = (position + roll) % 10 or 10

      updated_player_1 = (new_position, score + new_position) if player_1_turn else (player_1[0], player_1[1])
      updated_player_2 = (new_position, score + new_position) if not player_1_turn else (player_2[0], player_2[1])

      for i, won in enumerate(next_turn(updated_player_1, updated_player_2, not player_1_turn)): total_won[i] += won

    game_states[game_state] = total_won

    return total_won

  return next_turn(player_1, player_2)

def get_roll_combinations(sides) -> Tuple[int]:
  return tuple(sum(combination) for combination in product((range(1, sides + 1)), repeat=sides))

if __name__ == '__main__':
  (Puzzle('Day 21: Dirac Dice - part 2', CURRENT / 'input.txt')
    .add_test({ 'input_path': CURRENT / 'test.txt', 'expected_result': 444356092776315 })
    .add_test({ 'input_path': CURRENT / 'input.txt', 'expected_result': 272847859601291 })
    .solve(solve))
