from itertools import combinations

with open('9_input.txt') as f:
  xmas = [int(l) for l in f.readlines()]
xlen = len(xmas)
weakness = next(iter(xmas[pos] for pos in range(25, xlen) if xmas[pos] not in [sum(c) for c in combinations(xmas[pos-25 : pos], 2)]))
print 'part 1: %d' % weakness
print 'part 2: %d' % next(min(xmas[i:j]) + max(xmas[i:j]) for i in range(xlen-2) for j in range(i+2, xlen) if sum(xmas[i:j]) == weakness)

