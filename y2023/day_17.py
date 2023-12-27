from functools import partial
import importlib.util
import sys

spec = importlib.util.spec_from_file_location('a_star', '../a_star.py')
a_star = importlib.util.module_from_spec(spec)
sys.modules['a_star'] = a_star
spec.loader.exec_module(a_star)

data_files = [
  'day_17_input.txt',
  'day_17_test_input.txt'
]

def parse_data(filename):
  grid = [list(map(int, row)) for row in map(str.strip, open(filename).readlines())]
  w, h = len(grid[0]), len(grid)
  return grid, w, h

def neighbours(pos, w, h, max_n, min_n_to_steer=0):
  x,y,dx,dy,n = pos
  if (x,y) == (0,0):
    return [(0,1,0,1,1), (1,0,1,0,1)]
  if n < min_n_to_steer:
    dirs = set([(dx,dy)])
  else:
    dirs = set([(dy,dx), (-dy,-dx)] + ([] if n == max_n else [(dx,dy)]))
  return [(x+ndx, y+ndy, ndx, ndy, n+1 if ndx==dx and ndy==dy else 1)
          for ndx, ndy in dirs if 0 <= x+ndx < w and 0 <= y+ndy < h]

def traverse(data, neighbours):
  grid, w, h = data
  start = (0,0,0,0,0)  # x, y, dx, dy, num cells moved in this direction
  path = a_star.a_star(start = start,
                       is_finished = lambda p: p[0] == w-1 and p[1] == h-1,
                       heuristic = lambda p: w-1-p[0] + h-1-p[1],
                       neighbours = neighbours,
                       edge_weight = lambda p, np: grid[np[1]][np[0]])
  return sum(grid[y][x] for x,y,_,_,_ in path[1:])

def part1(data):
  _,w,h = data
  return traverse(data,
                  partial(neighbours, w=w, h=h, max_n=3))

def part2(data):
  _,w,h = data
  return traverse(data,
                  partial(neighbours, w=w, h=h, max_n=10, min_n_to_steer=4))

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 102 else '(failed)')
  p2_test = part2(data[-1])
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 94 else '(failed)')
  p1 = part1(data[0])
  print('Part 1:', p1)
  p2 = part2(data[0])
  print('Part 2:', p2)
