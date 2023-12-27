from itertools import accumulate

data_files = [
  'day_18_input.txt',
  'day_18_test_input.txt'
]

def parse_data(filename):
  lines = list(map(str.split, open(filename).readlines()))
  dirs_p1 = {
    'R': +1+0j,
    'D': +1j,
    'L': -1+0j,
    'U': -1j
  }
  part1 = list(accumulate(dirs_p1[direction] * int(dist)
                          for direction, dist, _ in lines))
  dirs_p2 = {
    '0': +1+0j,  # right
    '1': +1j,    # down
    '2': -1+0j,  # left
    '3': -1j,    # up
  }
  part2 = list(accumulate(dirs_p2[colour[7]] * int(colour[2:7], 16)
                          for _, _, colour in lines))
  return part1, part2

def fill_area(verts):
  return int(sum(v1.real * v2.imag - v1.imag * v2.real
                 + abs(v2.real - v1.real + v2.imag - v1.imag)
                 for v1,v2 in zip(verts, verts[1:] + [verts[0]]))) // 2 + 1

def part1(data):
  return fill_area(data[0])

def part2(data):
  return fill_area(data[1])

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 62 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 952408144115 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
