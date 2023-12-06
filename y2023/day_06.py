import math

def parse_data(filename):
  lines = open(filename).readlines()
  times = list(map(int, lines[0].split(':')[1].split()))
  distances = list(map(int, lines[1].split(':')[1].split()))
  return (times, distances)

data = parse_data('day_06_input.txt')
test_data = parse_data('day_06_test_input.txt')

def quadratic_roots(a, b, c):
  det = math.sqrt(b**2 - (4 * a * c))
  if det < 0:
    return []
  elif det == 0:
    return [-b / (2 * a)]
  else:
    return [(-b + det) / (2 * a), (-b - det) / (2 * a)]

def part1(test=False):
  times, distances = test_data if test else data
  product = 1
  for idx in range(len((times))):
    roots = quadratic_roots(-1, times[idx], -(distances[idx] + 1))
    product *= math.floor(roots[1]) - math.ceil(roots[0]) + 1
  return product

def part2(test=False):
  times, distances = test_data if test else data
  time = int(''.join(map(str, times)))
  distance = int(''.join(list(map(str, distances))))
  roots = quadratic_roots(-1, time, -(distance + 1))
  return math.floor(roots[1]) - math.ceil(roots[0]) + 1

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 288 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 71503 else '(failed)')
  print('Part 1:', part1())
  print('Part 2:', part2())
