from time import perf_counter()

def parse_data(filename):
  return open(filename).readlines()

st = perf_counter()
data = parse_data('day_N_input.txt')
parse_time = 1000 * (perf_counter() - st)
test_data = parse_data('day_N_test_input.txt') 

def part1(test=False):
  data = test_data if test else data

def part2(test=False):
  data = test_data if test else data

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  st = perf_counter()
  p1 = part1()
  p1_time = 1000 * (perf_counter() - st)
  st = perf_counter()
  p2 = part2()
  p2_time = 1000 * (perf_counter() - st)
  print('Data parse:', f'{parse_time:.4} ms')
  print('Part 1 test:', p1_test, '(passed)' if p1_test == <X> else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == None else '(failed)')
  print('Part 1:', p1, f'({p1_time:.4} ms)')
  print('Part 2:', p2, f'({p2_time:.4} ms)')
