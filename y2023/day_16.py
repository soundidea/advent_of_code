data_files = [
  # Add a 3rd entry if part 2 needs different test data.
  'day_16_input.txt',
  'day_16_test_input.txt'
]

LEFT = -1+0j
RIGHT = +1+0j
UP = 0-1j
DOWN = 0+1j

switches = {
  '.':  { LEFT:  [LEFT],
          RIGHT: [RIGHT],
          UP:    [UP],
          DOWN:  [DOWN] },
  '/':  { LEFT:  [DOWN],
          RIGHT: [UP],
          UP:    [RIGHT],
          DOWN:  [LEFT] },
  '\\': { LEFT:  [UP],
          RIGHT: [DOWN],
          UP:    [LEFT],
          DOWN:  [RIGHT] },
  '|':  { LEFT:  [UP, DOWN],
          RIGHT: [UP, DOWN],
          UP:    [UP],
          DOWN:  [DOWN] },
  '-':  { LEFT:  [LEFT],
          RIGHT: [RIGHT],
          UP:    [LEFT, RIGHT],
          DOWN:  [LEFT, RIGHT] }
}

def parse_data(filename):
  grid = list(map(list, map(str.strip, open(filename).readlines())))
  w, h = len(grid[0]), len(grid)
  return ({complex(x,y) : switches[c]
           for y,row in enumerate(grid)
           for x,c in enumerate(row)}, w, h)

def visit(switches, start_pos, start_dir):
  posdirs = [(start_pos, start_dir)]
  visited = set([posdirs[0]])
  while len(posdirs):
    new_posdirs = []
    for pos, dirn in posdirs:
      for newdir in switches[pos][dirn]:
        new_posdir = (pos + newdir, newdir)
        if new_posdir not in visited and new_posdir[0] in switches:
          new_posdirs.append(new_posdir)
          visited.add(new_posdir)
    posdirs = new_posdirs
  return len(set(pos for pos,_ in visited))

def part1(data):
  switches, _, _ = data
  return visit(switches, 0j, 1+0j)

def part2(data):
  switches, w, h = data
  return max(max(visit(switches, complex(x,0), DOWN) for x in range(w)),
             max(visit(switches, complex(x,h-1), UP) for x in range(w)),
             max(visit(switches, complex(0, y), RIGHT) for y in range(h)),
             max(visit(switches, complex(w-1, y), LEFT) for y in range(h)))

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 46 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == None else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
