import pathlib
from timeit import default_timer as timer

from typing import Any, Callable, List, TypedDict

class Test(TypedDict):
  input_path: pathlib.Path
  expected_result: str

class Puzzle:
  def __init__(self, name: str, input_path: pathlib.Path, tests: List[Test]=[]) -> None:
    self.name = name
    self.input_path = input_path
    self.tests = tests

  def solve_with(
    self,
    solver: Callable[[List[str]], Any],
    run_tests: bool=True
  ) -> str:
    print('--------------------------------------------------------')

    if run_tests:
      if not self.run_tests_with(solver):
        print()
        raise Exception('One or more tests failed!') 
      print()

    print(f'Solving puzzle: {self.name}\n')
    start = timer()
    solution = str(solver(self._read_input(self.input_path)))
    print(f'Solution: {solution} ({round(timer() - start, 3)}s)')

    print('--------------------------------------------------------')

    return solution

  def run_tests_with(
    self,
    solver: Callable[[List[str]], Any]
  ) -> bool:
    print(f'Running tests for puzzle: {self.name}\n')

    for test in self.tests:
      print(f"Testing for input: {test['input_path'].name}", end=' ')
      if not self._run_test_with(test, solver):
        return False

    print('\nAll tests passed!')
    return True

  def _run_test_with(self, test: Test, solver: Callable[[List[str]], Any]) -> bool:
    actual = str(solver(self._read_input(test['input_path'])))
    expected = test['expected_result']

    if actual != expected:
      print(f"FAILED! (expected={expected}, actual={actual})")
      return False

    print('PASSED!')
    return True

  def _read_input(self, path: pathlib.Path) -> List[str]:
    lines = []
    with open(path) as file:
      while (line := file.readline().rstrip()):
        lines.append(line)
    return lines
