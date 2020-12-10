from collections import Counter, defaultdict

with open('10_input.txt') as f:
  adapters = sorted(int(l) for l in f.readlines())
  adapters.append(adapters[-1] + 3)

c = Counter(b-a for a,b in zip([0] + adapters[:-1], adapters))
print 'part 1: %d' % (c[1] * c[3])

paths_to = defaultdict(int, {0: 1})
for a in adapters:
  paths_to[a] = sum(paths_to[a - i - 1] for i in range(3))
print 'part 2: %d' % combos[adapters[-1]]
