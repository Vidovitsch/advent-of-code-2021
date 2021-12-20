import pathlib
from typing import Any, List, Tuple, Union

from advent_helper.decorators import process_puzzle_input
from advent_helper.puzzle import Puzzle

PuzzleInput = Tuple[List[int], List[List[int]]]

def numbers_to_pixels(pixels: Union[List[int], List[List[int]]]):
  if isinstance(pixels[0], list):
    return [numbers_to_pixels(line) for line in pixels]
  else:
    return ''.join('.' if pixel == 0 else '#' for pixel in pixels)

def pixels_to_numbers(pixels: Union[str, List[str]]):
  if isinstance(pixels, str):
    return [0 if pixel == '.' else 1 for pixel in pixels]
  else:
    return [pixels_to_numbers(line) for line in pixels]

def process_input(input: List[str]) -> PuzzleInput:
  return pixels_to_numbers(input[0]), pixels_to_numbers(input[1:])

class Image:
  def __init__(self, image: List[List[int]], enhancement_algo: List[int]):
    self._image = image
    self.enhancement_algo = enhancement_algo

  def numbers_of_lit_pixels(self):
    lit_pixel_count = 0

    for line in self._image:
      for number in line:
        if number == 1: lit_pixel_count += 1
    
    return lit_pixel_count

  def show(self):
    print('\nImage:\n')
    for line in numbers_to_pixels(self._image):
      print(line)

@process_puzzle_input(process_input)
def solve(input: PuzzleInput) -> int:
  enhancement_algo, input_image = input
  image = Image(input_image, enhancement_algo)
  image.show()
  return image.numbers_of_lit_pixels()

if __name__ == '__main__':
  (Puzzle('Day 20 - Part 1', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 35 })
    .solve(solve))
