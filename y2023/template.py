data_files = [
  # Add a 3rd entry if part 2 needs different test data.
  'day_N_input.txt',
  'day_N_test_input.txt'
]

def parse_data(filename):
  return open(filename).readlines()

def part1(data):
  pass

def part2(data):
  pass

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == <X> else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == None else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
