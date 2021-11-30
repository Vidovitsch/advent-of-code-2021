import pathlib
from typing import Any, Callable, Generator

def read(
  path: pathlib.Path,
  line_processor: Callable[[str], Any]=lambda line: line,
) -> Generator[str, None, None]:
  with open(path) as file:
    while (line := file.readline().rstrip()):
      yield line_processor(line)
