from itertools import combinations

with open('09_input.txt') as f:
  xmas = list(map(int, f))

xlen = len(xmas)
weakness = next(iter(xmas[pos] for pos in range(25, xlen) if xmas[pos] not in [sum(c) for c in combinations(xmas[pos-25 : pos], 2)]))
print 'part 1: %d' % weakness

print 'part 2: %d' % next(min(xmas[i:j]) + max(xmas[i:j]) for i in range(xlen-2) for j in range(i+2, xlen) if sum(xmas[i:j]) == weakness)

# Much faster linear-time version of part 2 that I'm not clever enough to squish down into a pithy one liner:
i,j = 0,2
acc = sum(xmas[i:j])
while acc != weakness:
  acc += xmas[j]
  j += 1
  while acc > weakness and i < (j - 2):
    acc -= xmas[i]
    i += 1
print 'part 2: %d' % (min(xmas[i:j]) + max(xmas[i:j]))
