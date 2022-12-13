from functools import cmp_to_key
from math import prod

def compare(left, right, depth=0):
  if left == [] and right == []:
    return 0
  elif left == []:
    return -1
  elif right == []:
    return 1
  elif type(left) != type(right):
    if type(left) == int:
      return compare([left], right, depth + 1)
    else:
      return compare(left, [right], depth + 1)
  if type(left) == int:
    return -1 if left < right else (1 if right < left else 0)
  for l,r in zip(left, right):
    cmp = compare(l, r, depth + 1)
    if cmp != 0:
      return cmp
  if len(left) < len(right):
    return -1
  elif len(right) < len(left):
    return 1
  else:
    return 0

packets = [eval(p) for p in open('day13_input.txt').read().split('\n') if p != '']

pair_compares = [compare(l, r) for (l,r) in zip(packets[:-1:2], packets[1::2])]
print('part 1:', sum(idx+1
                     for idx,c in enumerate(pair_compares)
                     if c < 0))

dividers = [[[2]],[[6]]]
sorted_packets = sorted(packets + dividers, key=cmp_to_key(compare))
print('part 2:', prod(filter(lambda idx: sorted_packets[idx-1] in dividers,
                             range(1, 1 + len(sorted_packets)))))
