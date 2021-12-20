from functools import reduce
from itertools import chain,product
from operator import mul

hf = [[int(c) for c in line.strip()] for line in open('09_input.txt').readlines()]
w, h = len(hf[0]), len(hf)

def neighbour_coords(x, y):
  return [(xn,yn) for xn in [x - 1, x, x + 1]
                  for yn in [y - 1, y, y + 1]
                  if 0 <= xn < w and
                     0 <= yn < h and
                     (xn == x) ^ (yn == y)]

def min_neighbour(hf, x, y):
  return min(hf[y][x] for (x,y) in neighbour_coords(x, y))

low_points = list(filter(lambda c: hf[c[1]][c[0]] < min_neighbour(hf, *c),
                         product(range(w), range(h))))
print('part 1:', sum(hf[y][x] + 1 for (x,y) in list(low_points)))

def flood_size(hf, x, y):
  basin, next_basin = set(), set([(x,y)])
  while len(next_basin) > len(basin):
    basin, next_basin = (next_basin,
                         next_basin | set((xn,yn) for c in next_basin
                                                  for (xn,yn) in neighbour_coords(*c)
                                                  if hf[yn][xn] != 9))
  return len(basin)

print('part 2:', reduce(mul, sorted(flood_size(hf, *c) for c in low_points)[-3:]))
