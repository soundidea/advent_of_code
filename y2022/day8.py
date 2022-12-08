from math import prod
from functools import partial

def visibility(grid, coord, step):
  '''Walks the grid from coord in direction step.
     Stops if a tall enough tree is encountered.
     grid is a dict { Complex coord: Int tree height }
     Returns (Bool, Int) => (reached the edge?, num trees seen)'''
  n = 0
  h = grid[coord]
  coord += step
  while coord in grid:
    n += 1
    if grid[coord] >= h:
      return (False, n)
    coord += step
  return (True, n)

grid = {complex(x,y) : int(tree)
        for y,row in enumerate(open('day8_input.txt').read().split('\n'))
        for x,tree in enumerate(row)}
trees = [[partial(visibility, grid, c)(step) for step in (-1, 1, -1j, 1j)] for c in grid]
print('part 1:', sum(any(direction[0] for direction in tree) for tree in trees))
print('part 2:', max(prod(direction[1] for direction in tree) for tree in trees))
