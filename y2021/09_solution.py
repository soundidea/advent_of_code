from itertools import chain,product

def neighbour_coords(w, h, x, y):
  return chain([(x - 1, y)] if x > 0 else [],
               [(x, y - 1)] if y > 0 else [],
               [(x + 1, y)] if x < w - 1 else [],
               [(x, y + 1)] if y < h - 1 else [])
from functools import reduce
from operator import mul

def min_neighbour(hf, w, h, x, y):
  return min(hf[y][x] for (x,y) in neighbour_coords(w, h, x, y))

hf = [[int(c) for c in line.strip()] for line in open('09_input.txt').readlines()]
w, h = len(hf[0]), len(hf)
low_points = list(filter(lambda c: hf[c[1]][c[0]] < min_neighbour(hf, w, h, c[0], c[1]),
                         product(range(w), range(h))))
print('part 1:', sum(hf[y][x] + 1 for (x,y) in list(low_points)))

def flood_size(hf, w, h, x, y):
  flooded_coords = set([(x,y)])
  while True:
    basin_neighbours = set((xn,yn) for c in flooded_coords
                                   for (xn,yn) in neighbour_coords(w, h, *c)
                                   if hf[yn][xn] != 9)
    new_coords = basin_neighbours - flooded_coords
    if len(new_coords) == 0:
      break
    flooded_coords |= new_coords
  return len(flooded_coords)

print('part 2:', reduce(mul, sorted(flood_size(hf, w, h, *c) for c in low_points)[-3:]))
