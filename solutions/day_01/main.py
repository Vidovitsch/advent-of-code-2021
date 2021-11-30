from os import path
import pathlib

from advent_helper import input_reader

def get_input_path() -> pathlib.Path:
  return pathlib.Path(__file__).parent / 'input.txt'


if __name__ == '__main__':
  print([i for i in input_reader.read(get_input_path())])
