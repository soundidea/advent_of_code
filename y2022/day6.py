def find_first_unique(n, signal):
  return next(filter(lambda pos: len(set(signal[pos:pos+n])) == n,
                     range(len(signal) - n))) + n

signal = open('day6_input.txt').read().strip()
print('part 1:', find_first_unique(4, signal))
print('part 2:', find_first_unique(14, signal))
