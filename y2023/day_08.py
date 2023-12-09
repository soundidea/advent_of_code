from functools import reduce
from itertools import cycle
from math import lcm

data_files = [
  # Add a 3rd entry if part 2 needs different test data.
  'day_08_input.txt',
  'day_08_test_input.txt',
  'day_08_test_input_2.txt'
]

def value(node):
  return ord(node[0])*128*128 + ord(node[1])*128 + ord(node[2])

def parse_data(filename):
  lines = open(filename).readlines()
  directions = [0 if c == 'L' else 1 for c in lines[0][:-1]]
  nodes = {value(l[:3]) : (value(l[7:10]), value(l[12:15])) for l in lines[2:]}
  return directions, nodes

cached_traversals = {}

def traverse(start, nodes, directions):
  if start in cached_traversals:
    return cached_traversals[start]
  n, end = start, ord('Z')
  for num_steps, direction in enumerate(cycle(directions)):
    n = nodes[n][direction]
    if n%128 == end:
      cached_traversals[start] = num_steps + 1
      return num_steps + 1

def part1(data):
  directions, nodes = data
  return traverse(value('AAA'), nodes, directions)

def part2(data):
  directions, nodes = data
  start_nodes = [n for n in nodes if n%128 == ord('A')]
  return reduce(lambda result, n: lcm(result,
                                      traverse(n, nodes, directions)), 
                start_nodes, 1)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  cached_traversals = {}
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 6 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 6 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
