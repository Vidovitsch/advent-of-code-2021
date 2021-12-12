import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 12 - Part 1',
    pathlib.Path(__file__).parent / 'input.txt',
    [
      {
        'input_path': pathlib.Path(__file__).parent / 'test1.txt',
        'expected_result': '10'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'test2.txt',
        'expected_result': '19'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'test3.txt',
        'expected_result': '226'
      },
      {
        'input_path': pathlib.Path(__file__).parent / 'input.txt',
        'expected_result': '3292'
      }
    ]
  )

def run():
  get_puzzle().solve_with(solve, process_input)

##############################################################
# Solution
##############################################################

def process_input(line):
  return line.split('-')

def solve(input):
  graph = create_bidrected_graph(input)
  return traverse(graph)

def traverse(graph, root='start', visited=[]):
  if root == 'end':
    return 1

  linked_nodes = [node for node in graph[root] if node not in visited]

  if len(linked_nodes) == 0:
    return 0

  reached_end_count = 0

  for node in linked_nodes:
    extended_visited = [i for i in visited]
    if root.islower():
      extended_visited = visited + [root]
    reached_end_count += traverse(graph, node, extended_visited)
  
  return reached_end_count

def create_bidrected_graph(input):
  graph = {}

  def add(node1, node2):
    if node1 not in graph:
      graph[node1] = []
    graph[node1].append(node2)

  for node1, node2 in input:
    add(node1, node2)
    add(node2, node1)

  return graph


if __name__ == '__main__':
  run()
