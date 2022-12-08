from itertools import takewhile
from math import prod

def rays(x,y,w,h,grid):
  return (
    [grid[y][rx] for rx in range(x-1, -1, -1)],  # left from x
    [grid[y][rx] for rx in range(x+1, w)],       # right from x
    [grid[ry][x] for ry in range(y-1, -1, -1)],  # up from y
    [grid[ry][x] for ry in range(y+1, h)])       # down from y

def num_can_see(h, seq):
  return min(len(seq), 1 + len(list(takewhile(lambda tree: tree < h, seq))))

grid = [list(map(int, row.strip())) for row in open('day8_input.txt').readlines()]
w,h = len(grid[0]), len(grid)
print('part 1:', sum(any(max(ray) < grid[y][x] if len(ray) else True
                         for ray in rays(x,y,w,h,grid))
                     for x in range(w)
                     for y in range(h)))
print('part 2:', max(prod(num_can_see(grid[y][x], ray)
                          for ray in rays(x,y,w,h,grid))
                     for x in range(w)
                     for y in range(h)))

