from functools import reduce
from math import lcm
from time import perf_counter

def parse_data(filename):
  lines = open(filename).readlines()
  directions = [0 if c == 'L' else 1 for c in lines[0][:-1]]
  nodes = {l[:3] : (l[7:10], l[12:15]) for l in lines[2:]}

  # last_visited = for each node, maps to the node you reach if you follow the directions once.
  last_visited = {node: reduce(lambda n,d: nodes[n][d], directions, node) for node in nodes}
  return last_visited, len(directions)

st = perf_counter()
data = parse_data('day_08_input.txt')
parse_time = 1000 * (perf_counter() - st)

def part1(test=False):
  last_visited, num_directions = parse_data('day_08_test_input.txt') if test else data
  # 'ZZZ' is only ever reached after len(directions) steps from other nodes
  # given node, which is super convenient.
  node, num_steps = 'AAA', 0
  while node != 'ZZZ':
    node, num_steps = last_visited[node], num_steps + 1
  return num_steps * num_directions

def part2(test=False):
  last_visited, num_directions = parse_data('day_08_test_input_2.txt') if test else data
  start_nodes = [n for n in last_visited if n[2] == 'A']
  result = 1
  for node in start_nodes:
    # 'xxZ' always happens to be at the end of a repeating cycle that is
    # exactly N * len(directions) long. How useful...
    num_steps = 0
    while node[2] != 'Z':
      node, num_steps = last_visited[node], num_steps + 1
    result = lcm(result, num_steps * num_directions)
  return result

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
