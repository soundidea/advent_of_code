
def parse_data(filename):
  lines = open(filename).readlines()
  times = list(map(int, lines[0].split(':')[1].split()))
  distances = list(map(int, lines[1].split(':')[1].split()))
  return (times, distances)

data = parse_data('day_06_input.txt')
test_data = parse_data('day_06_test_input.txt')

def part1(test=False):
  times, distances = test_data if test else data
  product = 1
  for idx,t in enumerate(times):
    product *= sum((t-i)*i > distances[idx] for i in range(1,t))
  return product

def part2(test=False):
  times, distances = test_data if test else data
  time = int(''.join(map(str, times)))
  distance = int(''.join(list(map(str, distances))))
  return sum((time-i)*i > distance for i in range(1,time))

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 288 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 71503 else '(failed)')
  print('Part 1:', part1())
  print('Part 2:', part2())
