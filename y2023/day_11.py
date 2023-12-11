from bisect import bisect_left
from itertools import combinations

data_files = [
  'day_11_input.txt',
  'day_11_test_input.txt'
]

def parse_data(filename):
  data = open(filename).readlines()
  h, w = len(data), len(data[0]) - 1
  galaxies = set(complex(x,y)
                 for y,row in enumerate(data)
                 for x,cell in enumerate(row)
                 if cell == '#')
  row_gaps = [y for y in range(h) if y not in map(lambda c: int(c.imag), galaxies)]
  col_gaps = [x for x in range(w) if x not in map(lambda c: int(c.real), galaxies)]
  return (galaxies, row_gaps, col_gaps)

def manhattan_dist(p1, p2):
  return int(abs(p1.real - p2.real) + abs(p1.imag - p2.imag))

def sum_of_distances(galaxies, row_gaps, col_gaps, expansion_amount=2):
  expanded_galaxies = set(complex(g.real + 1 + (expansion_amount-1) * bisect_left(col_gaps, g.real),
                                  g.imag + 1 + (expansion_amount-1) * bisect_left(row_gaps, g.imag))
                          for g in galaxies)
  return sum(manhattan_dist(g1, g2) for g1,g2 in combinations(expanded_galaxies, 2))


def part1(data):
  return sum_of_distances(*data)

def part2(data, expansion_amount=1000000):
  return sum_of_distances(*data, expansion_amount=expansion_amount)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test_10 = part2(data[-1], 10)
  p2_test_100 = part2(data[-1], 100)
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 374 else '(failed)')
  print('Part 2 test (10):', p2_test_10, '(passed)' if p2_test_10 == 1030 else '(failed)')
  print('Part 2 test (100):', p2_test_100, '(passed)' if p2_test_100 == 8410 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
