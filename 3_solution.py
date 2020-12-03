from functools import partial


def trees_for_slope(g, (dx,dy)):
  return sum(1 for y in range(0, len(g), dy) if g[y][(dx * y / dy) % len(g[0])] == '#')


def product(seq):
  return reduce(lambda a, b: a * b, seq)


if __name__ == '__main__':
  with open('3_input.txt') as f:
    grid = [l.rstrip() for l in f.readlines()]
  print 'part 1: %d' % trees_for_slope(grid, (3,1))
  print 'part 2: %d' % product(map(partial(trees_for_slope, grid), [(1,1), (3,1), (5,1), (7,1), (1,2)]))
