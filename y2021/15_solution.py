def neighbours(x,y,w,h):
  return set((xn,yn) for xn in [x - 1, x, x + 1]
                     for yn in [y - 1, y, y + 1]
                     if (xn == x) ^ (yn == y) and
                        0 <= xn < w and
                        0 <= yn < h)

def cost_to_exit(cave):
  w, h = len(cave[0]), len(cave)
  costs = [[(w+h)*9 if x+y else 0 for x in range(w)] for y in range(h)]
  to_visit = set((x,y) for x in range(w) for y in range(h) if x+y != 0)
  while len(to_visit):
    next_visit = set()
    for x,y in to_visit:
      neigh = neighbours(x,y,w,h)
      cheapest_neighbour = min(costs[yn][xn] for xn,yn in neigh)
      cost = cave[y][x] + cheapest_neighbour
      if cost < costs[y][x]:
        costs[y][x] = cost
        next_visit |= neigh
    to_visit = next_visit
  return costs[h-1][w-1]

def generate_full_cave(cave):
  w, h = len(cave[0]), len(cave)
  return [[((cave[y % h][x % w] + y // h + x // w - 1) % 9) + 1
           for x in range(5 * w)]
          for y in range(5 * h)]

cave = [list(map(int, (line.strip()))) for line in open('15_input.txt').readlines()]
print('part 1:', cost_to_exit(cave))
print('part 2:', cost_to_exit(generate_full_cave(cave)))
