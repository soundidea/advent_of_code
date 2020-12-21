import re
from itertools import chain

with open('21_input.txt') as f:
  foods = [l.split('(contains ') for l in f]
  foods = [(set(i.split()), a.rstrip(')\n').split(', ')) for i,a in foods]

allergens = set(chain.from_iterable(a for (_,a) in foods))
candidates = {allergen: reduce(set.intersection, [i for i,a in foods if allergen in a]) for allergen in allergens}
allergens = {}
while len(candidates):
  a = next(a for (a,i) in candidates.items() if len(i) == 1)
  i = list(candidates.pop(a))[0]
  allergens[a] = i
  candidates = {a2: i2.difference([i]) for a2, i2 in candidates.items()}

print 'part 1:', sum(map(len, iter(i.difference(allergens.values()) for (i,_) in foods)))
print 'part 2:', ','.join(allergens[a] for a in sorted(allergens.keys()))

