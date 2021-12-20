import pathlib
from timeit import default_timer as timer
from typing import Any, Callable, List, Tuple, TypedDict

from advent_helper.colors import END, GREEN, ORANGE, RED, UNDERLINE

class Test(TypedDict):
  input_path: pathlib.Path
  expected_result: str

class Puzzle:
  def __init__(self, name: str, input_path: pathlib.Path) -> None:
    self.name = name
    self.input_path = input_path

    self.tests = []

  def add_test(self, test: Test) -> 'Puzzle':
    self.tests.append(test)

    return self

  def solve(self, solve: Callable[[Any], Any]) -> Any:
    print(f'\n🧩 {ORANGE}{self.name}{END} 🧩')

    if self.tests:
      print()
      if not self._run_all_tests(solve):
        print(f'\n{RED}Not all tests passed!{END} 💣💥')
        return

    puzzle_input = self._read_input(self.input_path)
    solution, time = self._solve_and_time(solve, puzzle_input)

    print('\n⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️')
    print(f'\nSolution: {ORANGE}{solution}{END} (in {ORANGE}{time}s{END})')
    print('\n⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️')

    return solution

  def _read_input(self, path: pathlib.Path) -> List[str]:
    with open(path) as file:
      lines = (line.rstrip() for line in file)
      return list(line for line in lines if line)

  def _run_all_tests(self, solve: Callable[[Any], Any]) -> bool:
    return all([self._run_test(test, solve) for test in self.tests])

  def _run_test(self, test: Test, solve: Callable[[Any], Any]) -> bool:
      print(f"🧪 Test from input file {UNDERLINE}{test['input_path'].name}{END}", end=' -> ')

      test_input = self._read_input(test['input_path'])
      actual, time = self._solve_and_time(solve, test_input)
      expected = test['expected_result']

      if actual != expected:
        print(f'{RED}FAILED!{END} (in {ORANGE}{time}s{END}) [expected={expected} actual={actual}]')
        return False
      else:
        print(f'{GREEN}PASSED!{END} (in {ORANGE}{time}s{END})')
        return True
  
  def _solve_and_time(self, solve: Callable[[Any], Any], input: List[str]) -> Tuple[Any, float]:
    start = timer()
    solution = solve(input)
    end = timer()

    return solution, round(end - start, 6)
