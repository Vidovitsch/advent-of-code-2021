import pathlib

from advent_helper.puzzle import Puzzle

import part_1
import part_2

def solve_part_1():
  (Puzzle('Day 15 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .set_input_processor(part_1.process_input)
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': -1 })
    .solve(part_1.solve))

def solve_part_2():
  (Puzzle('Day 15 - Part 2', pathlib.Path(__file__).parent / 'input.txt')
    .set_input_processor(part_2.process_input)
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': -1 })
    .solve(part_2.solve))

if __name__ == '__main__':
  solve_part_1()
  solve_part_2()
