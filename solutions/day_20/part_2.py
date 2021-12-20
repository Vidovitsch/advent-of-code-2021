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

def index(value, list):
  try:
    return list.index(value)
  except ValueError:
    return None

class Image:
  def __init__(self, image: List[List[int]], enhancement_algo: List[int]):
    self._image = image
    self.enhancement_algo = enhancement_algo
    self.frame_pixel = 0

  def enhance(self):
    frame_size = 1
    enhanced_image = self.add_frame(frame_size, self.frame_pixel)._copy()

    for row in range(len(self._image)):
      for col in range(len(self._image[0])):
        binary_number = ''

        for i in (-1, 0, 1):
          for j in (-1, 0, 1):
            if 0 <= row + i < len(self._image) and 0 <= col + j < len(self._image[0]):
              binary_number += str(self._image[row + i][col + j])
            else:
              binary_number += str(self.frame_pixel)

        enhanced_image[row][col] = self.enhancement_algo[int(binary_number, 2)]
    
    self._image = enhanced_image
    if self.frame_pixel == 0:
      self.frame_pixel = self.enhancement_algo[0]
    else:
      self.frame_pixel = self.enhancement_algo[-1]

    return self

  def add_frame(self, frame_size, pixel=0):
    image_with_frame = []

    for i in range(-frame_size, len(self._image) + frame_size):
      if 0 <= i < len(self._image):
        image_with_frame.append([pixel] * frame_size + self._image[i] + [pixel] * frame_size)
      else:
        image_with_frame.append([pixel] * (len(self._image[0]) + frame_size * 2))
    
    self._image = image_with_frame

    return self

  def show(self):
    print('\nImage:\n')
    for line in numbers_to_pixels(self._image):
      print(line)
    print()

  def number_of_lit_pixels(self):
    lit_pixel_count = 0

    for line in self._image:
      for number in line:
        if number == 1: lit_pixel_count += 1
    
    return lit_pixel_count

  def _copy(self):
    copy = []

    for i in range(len(self._image)):
      row = []
      for j in range(len(self._image[0])):
        row.append(self._image[i][j])
      copy.append(row)
  
    return copy

@process_puzzle_input(process_input)
def solve(input: PuzzleInput) -> int:
  enhancement_algo, input_image = input
  image = Image(input_image, enhancement_algo)

  enhancement_count = 50

  for _ in range(enhancement_count):
    image.enhance()

  return image.number_of_lit_pixels()

if __name__ == '__main__':
  (Puzzle('Day 20 - Part 2', pathlib.Path(__file__).parent / 'input.txt')
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'test.txt', 'expected_result': 3351 })
    .add_test({ 'input_path': pathlib.Path(__file__).parent / 'input.txt', 'expected_result': 19012 })
    .solve(solve))
