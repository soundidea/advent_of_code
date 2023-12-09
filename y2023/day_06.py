import math

data_files = [
  'day_06_input.txt',
  'day_06_test_input.txt'
]

def parse_data(filename):
  lines = open(filename).readlines()
  times = list(map(int, lines[0].split(':')[1].split()))
  distances = list(map(int, lines[1].split(':')[1].split()))
  return (times, distances)

def quadratic_roots(a, b, c):
  det = math.sqrt(b**2 - (4 * a * c))
  if det < 0:
    return []
  elif det == 0:
    return [-b / (2 * a)]
  else:
    return [(-b + det) / (2 * a), (-b - det) / (2 * a)]

def part1(data):
  times, distances = data
  product = 1
  for idx in range(len((times))):
    roots = quadratic_roots(-1, times[idx], -(distances[idx] + 1))
    product *= math.floor(roots[1]) - math.ceil(roots[0]) + 1
  return product

def part2(data):
  times, distances = data
  time = int(''.join(map(str, times)))
  distance = int(''.join(list(map(str, distances))))
  roots = quadratic_roots(-1, time, -(distance + 1))
  return math.floor(roots[1]) - math.ceil(roots[0]) + 1

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 288 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 71503 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
