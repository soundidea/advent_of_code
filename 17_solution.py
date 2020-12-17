from itertools import product
import numpy as np

def neighbours(coord):
  dims = len(coord)
  return map(tuple, np.add(coord, [d for d in product([-1,0,1], repeat=dims) if d != tuple([0]*dims)]))

def set_active(grid, coord):
  num_active_neighbours = sum(1 for n in neighbours(coord) if n in grid)
  is_currently_active = coord in grid
  return (is_currently_active and 2 <= num_active_neighbours <= 3) \
      or (not is_currently_active and num_active_neighbours == 3)

def limits(grid):
  dims = len(next(iter(grid)))
  return [(min(c[axis] for c in grid), 1 + max(c[axis] for c in grid)) for axis in range(dims)]

with open('17_input.txt') as f:
  grid = set((x,y,0) for y,row in enumerate(f) for x,cell in enumerate(row) if cell == '#')
one_turn = lambda grid,_: set(c for c in product(*map(lambda (l1,l2): range(l1-1,l2+1), limits(grid))) if set_active(grid, c))
print 'part 1: %d' % len(reduce(one_turn, range(6), grid))
print 'part 2: %d' % len(reduce(one_turn, range(6), set(g + (0,) for g in grid)))
