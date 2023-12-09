from functools import reduce

data_files = [
  # Add a 3rd entry if part 2 needs different test data.
  'day_09_input.txt',
  'day_09_test_input.txt'
]

def diffchain(sequence):
  chain, prev = [sequence], sequence
  while prev[-1]:
    prev = [prev[i+1] - p for i,p in enumerate(prev[:-1])]
    if prev[-1]:
      chain.append(prev)
  return chain

def parse_data(filename):
  sequences = [list(map(int,l.split())) for l in open(filename).readlines()]
  return [diffchain(seq) for seq in sequences]

def part1(chains):
  return sum(sum(c[-1] for c in chain) for chain in chains)

def part2(chains):
  return sum(reduce(lambda extend, seq: seq[0] - extend, chain[::-1], 0)
             for chain in chains)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 114 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 2 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
