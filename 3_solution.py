from functools import partial


def gen_coords((dx,dy), max_x, max_y):
  return zip(map(lambda x: x % max_x, range(0, max_y * dx / dy, dx)), range(0, max_y, dy))


def trees_for_slope(grid, (dx,dy)):
  return sum(1 for (x,y) in gen_coords((dx,dy), len(grid[0]), len(grid)) if grid[y][x] == '#')


def product(seq):
  return reduce(lambda a, b: a * b, seq)


if __name__ == '__main__':
  with open('3_input.txt') as f:
    grid = [l.rstrip() for l in f.readlines()]
  print 'part 1: %d' % trees_for_slope(grid, (3,1))
  print 'part 2: %d' % product(map(partial(trees_for_slope, grid), [(1,1), (3,1), (5,1), (7,1), (1,2)]))
