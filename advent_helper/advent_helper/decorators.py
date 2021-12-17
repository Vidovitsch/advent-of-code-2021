from typing import Any, Callable, List

def process_puzzle_input(process: Callable[[List[str]], Any]) -> Callable:
  def decorator(func: Callable[[Any], Any]) -> Callable:
    def wrapper(input: List[str]) -> Any:
      return func(process(input))
    return wrapper
  return decorator
