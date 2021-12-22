from collections import defaultdict
from heapq import *
import math

def neighbours(x,y,w,h):
  return [(xn,yn) for xn in [x - 1, x, x + 1]
                  for yn in [y - 1, y, y + 1]
                  if (xn == x) ^ (yn == y) and
                     0 <= xn < w and
                     0 <= yn < h]

def cost_to_exit(cave):
  '''Perform an A-star search to find the cheapest cost through the cave.'''
  w,h = len(cave[0]), len(cave)
  start, goal = (0,0), (w-1,h-1)
  open_set = []
  heappush(open_set, (w+h, start))
  costs = defaultdict(lambda:math.inf)
  costs[start] = 0
  reads, writes = 0, 1
  while len(open_set):
    reads += 1
    _,pos = heappop(open_set)
    if pos == goal:
      return costs[pos]
    p_cost = costs[pos]
    for n in neighbours(*pos,w,h):
      n_cost, cost = costs[n], p_cost + cave[n[1]][n[0]]
      if cost < n_cost:
        writes += 1
        costs[n] = cost
        heappush(open_set, (cost + w + h - sum(n), n))

def generate_full_cave(cave):
  w, h = len(cave[0]), len(cave)
  return [[((cave[y % h][x % w] + y // h + x // w - 1) % 9) + 1
           for x in range(5 * w)]
          for y in range(5 * h)]

cave = [list(map(int, (line.strip()))) for line in open('15_input.txt').readlines()]
print('part 1:', cost_to_exit(cave))
print('part 2:', cost_to_exit(generate_full_cave(cave)))
