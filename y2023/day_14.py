data_files = [
  'day_14_input.txt',
  'day_14_test_input.txt'
]

GAP, ROCK, CUBE = 0,1,2

def parse_data(filename):
  conv = {'.' : GAP, 'O' : ROCK, '#' : CUBE}
  grid = [[conv[c] for c in row] 
          for row in map(str.strip, open(filename).readlines())]
  return grid

def tilt_ns(grid, north=True):
  sz = len(grid)  # grid is square, nice
  d = 1 if north else -1
  for x in range(sz):
    to = 0 if north else sz-1
    for y in range(sz) if north else range(sz-1,-1,-1):
      c = grid[y][x]
      if c == ROCK:
        if to != y:
          grid[to][x], grid[y][x] = grid[y][x], grid[to][x]
        to += d
      elif c == CUBE:
        to = y + d
  return grid

def tilt_ew(grid, west=True):
  sz = len(grid)  # grid is square, nice
  d = 1 if west else -1
  for y in range(sz):
    to = 0 if west else sz-1
    for x in range(sz) if west else range(sz-1,-1,-1):
      c = grid[y][x]
      if c == ROCK:
        if to != x:
          grid[y][to], grid[y][x] = grid[y][x], grid[y][to]
        to += d
      elif c == CUBE:
        to = x + d
  return grid

def load_on_north_beam(grid):
  sz = len(grid)
  return sum((sz-y) * row.count(ROCK) for y,row in enumerate(grid))

def part1(data):
  return load_on_north_beam(tilt_ns(data, north=True))

def part2(data):
  grid = data
  num_cycles = 1000000000
  state_cycle_map = dict()
  for cycle in range(num_cycles):
    data = tilt_ns(data, north=True)  # tilt north
    data = tilt_ew(data, west=True)   # tilt west
    data = tilt_ns(data, north=False) # tilt south
    data = tilt_ew(data, west=False)  # tilt east
    state = tuple(map(tuple, data))
    if not state in state_cycle_map:
      # No loop found yet
      state_cycle_map[state] = cycle
      continue
    loop_start = state_cycle_map[state]
    loop_len = cycle - loop_start
    final_idx = ((num_cycles - loop_start - 1) % loop_len) + loop_start
    return next(load_on_north_beam(state)
                for state,cycle in state_cycle_map.items()
                if cycle == final_idx)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 136 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 64 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
