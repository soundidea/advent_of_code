from functools import reduce
from itertools import cycle
from math import lcm
from time import perf_counter

def value(node):
  return ord(node[0])*128*128 + ord(node[1])*128 + ord(node[2])

def parse_data(filename):
  lines = open(filename).readlines()
  directions = [0 if c == 'L' else 1 for c in lines[0][:-1]]
  nodes = {value(l[:3]) : (value(l[7:10]), value(l[12:15])) for l in lines[2:]}
  return directions, nodes

st = perf_counter()
data = parse_data('day_08_input.txt')
parse_time = 1000 * (perf_counter() - st)

cached_traversals = {}

def traverse(start, nodes, directions, test):
  if start in cached_traversals:
    return cached_traversals[start]
  n, end = start, ord('Z')
  for num_steps, direction in enumerate(cycle(directions)):
    n = nodes[n][direction]
    if n%128 == end:
      if not test:
        cached_traversals[start] = num_steps + 1
      return num_steps + 1

def part1(test=False):
  directions, nodes = parse_data('day_08_test_input.txt') if test else data
  return traverse(value('AAA'), nodes, directions, test)

def part2(test=False):
  directions, nodes = parse_data('day_08_test_input_2.txt') if test else data
  start_nodes = [n for n in nodes if n%128 == ord('A')]
  return reduce(lambda result, n: lcm(result,
                                      traverse(n, nodes, directions, test)), 
                start_nodes, 1)

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  st = perf_counter()
  p1 = part1()
  p1_time = 1000 * (perf_counter() - st)
  st = perf_counter()
  p2 = part2()
  p2_time = 1000 * (perf_counter() - st)
  print('Data parse:', f'{parse_time:.4} ms')
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 6 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 6 else '(failed)')
  print('Part 1:', p1, f'({p1_time:.4} ms)')
  print('Part 2:', p2, f'({p2_time:.4} ms)')
