import re

data_files = [
  'day_10_input.txt',
  'day_10_test_input.txt',
  'day_10_test_input_2.txt'
]

neighbours = {'|': (0-1j, 0+1j),
              '-': (-1+0j, 1+0j),
              'L': (1+0j, 0-1j),
              'J': (-1+0j, 0-1j),
              '7': (-1+0j, 0+1j),
              'F': (1+0j, 0+1j)}

def lookup(data, cell, offset=0j):
  cell += offset
  return data[int(cell.imag)][int(cell.real)]

def cell_type(cell, data):
  above = lookup(data, cell, -1j) in ['|', '7', 'F']
  below = lookup(data, cell, +1j) in ['|', 'L', 'J']
  left  = lookup(data, cell, -1+0j) in ['-', 'L', 'F']
  right = lookup(data, cell, +1+0j) in ['-', '7', 'J']
  if above and below:
    return '|'
  if left and right:
    return '-'
  if above and left:
    return 'J'
  if above and right:
    return 'L'
  if below and left:
    return '7'
  if below and right:
    return 'F'

def parse_data(filename):
  data = list(map(str.strip, open(filename).readlines()))
  for y,row in enumerate(data):
    for x,cell in enumerate(row):
      if cell == 'S':
        animal_start = complex(x,y)
        data[y] = row[:x] + cell_type(animal_start, data) + row[x+1:]
        return data, animal_start

def traverse_loop(data, start):
  prev_pos, pos = start, start + neighbours[lookup(data, start)][0]
  loop = set([start])
  while pos != start:
    loop.add(pos)
    prev_pos, pos = pos, pos + next(filter(lambda n: pos+n != prev_pos,
                                           neighbours[lookup(data, pos)]))
  return loop

cached_loop_coords = set()

def part1(data):
  data, animal_start = data
  global cached_loop_coords
  cached_loop_coords = traverse_loop(data, animal_start)
  return len(cached_loop_coords) // 2

def part2(data):
  only_loop = [''.join(cell if complex(x,y) in cached_loop_coords else '.'
                       for x,cell in enumerate(row))
               for y,row in enumerate(data[0])]
  edge_re = re.compile(r'\||F-*J|L-*7')
#  for row in only_loop:
#    carved = edge_re.split(row)
#    print(row, carved)
  return sum(sum(i.count('.') for i in edge_re.split(row)[1::2]) for row in only_loop)
    

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  part1(data[-1])  # Just to cache the loop coords for p2 test
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 8 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 10 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
