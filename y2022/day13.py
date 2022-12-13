from functools import cmp_to_key
from math import prod

def compare(left, right):
  if type(left) != type(right):
    return compare([left] if type(left) != list else left,
                   [right] if type(right) != list else right)
  if type(left) == int:
    return -1 if left < right else (1 if right < left else 0)
  for l,r in zip(left, right):
    cmp = compare(l, r)
    if cmp != 0:
      return cmp
  return (-1 if len(left) < len(right)
             else (1 if len(right) < len(left)
                     else 0))

packets = [eval(p)
           for p in open('day13_input.txt').read().split('\n')
           if p != '']

pair_comps = [compare(l, r) for (l,r) in zip(packets[:-1:2], packets[1::2])]
print('part 1:', sum(idx+1
                     for idx,c in enumerate(pair_comps)
                     if c < 0))

dividers = [[[2]],[[6]]]
sorted_packets = sorted(packets + dividers, key=cmp_to_key(compare))
print('part 2:', prod(map(lambda p: p[0]+1,
                          filter(lambda p: p[1] in dividers,
                                 enumerate(sorted_packets)))))
