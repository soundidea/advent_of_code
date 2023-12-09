from functools import reduce
from time import perf_counter

def diffchain(sequence):
  chain, prev, l = [sequence], sequence, len(sequence)
  while True:
    l -= 1
    prev = [prev[idx+1] - prev[idx] for idx in range(l)]
    if not prev[-1]:
      break
    chain.append(prev)
  return chain

def parse_data(filename):
  sequences = [list(map(int,l.split())) for l in open(filename).readlines()]
  return [diffchain(seq) for seq in sequences]

st = perf_counter()
data = parse_data('day_09_input.txt')
parse_time = 1000 * (perf_counter() - st)
test_data = parse_data('day_09_test_input.txt') 

def part1(test=False):
  chains = test_data if test else data
  return sum(sum(c[-1] for c in chain) for chain in chains)

def part2(test=False):
  chains = test_data if test else data
  return sum(reduce(lambda extend, seq: seq[0] - extend, chain[::-1], 0)
             for chain in chains)

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
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 114 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 2 else '(failed)')
  print('Part 1:', p1, f'({p1_time:.4} ms)')
  print('Part 2:', p2, f'({p2_time:.4} ms)')
