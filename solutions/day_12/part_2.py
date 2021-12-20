import pathlib
import math

from advent_helper import puzzle

def get_puzzle() -> puzzle.Puzzle:
  return puzzle.Puzzle(
    'Day 12 - Part 2',
    CURRENT / 'input.txt',
    [
      {
        'input_path': CURRENT / 'test1.txt',
        'expected_result': '36'
      },
      {
        'input_path': CURRENT / 'test2.txt',
        'expected_result': '103'
      },
      {
        'input_path': CURRENT / 'test3.txt',
        'expected_result': '3509'
      },
      {
        'input_path': CURRENT / 'input.txt',
        'expected_result': '89592'
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
  unique_data = [list(x) for x in set(tuple(x) for x in traverse(graph))]
  return len(unique_data)

def traverse(graph, root='start', visited=[], allowed_twice=None, path=[]):
  new_path = path + [root]
  if root == 'end':
    return [new_path]

  linked_nodes = [node for node in graph[root] if node not in visited]

  if len(linked_nodes) == 0:
    return []

  reached_end_paths = []

  for node in linked_nodes:
    extended_visited = [i for i in visited]
    if root.islower():
      if not allowed_twice and root != 'start':
        reached_end_paths += traverse(graph, node, [i for i in visited], root, new_path)
      extended_visited = visited + [root]
    reached_end_paths += traverse(graph, node, extended_visited, allowed_twice, new_path)
  
  return reached_end_paths

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
