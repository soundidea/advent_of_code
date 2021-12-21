from functools import reduce
import re

coords, folds = [line.strip().split('\n')
                 for line in open('13_input.txt').read().split('\n\n')]
coords = set(tuple(map(int, re.match(r'(\d+),(\d+)', coord).groups()))
             for coord in coords)
folds = [({'x': 0, 'y': 1}[a], int(b))
          for a,b in [re.match(r'fold along ([xy])=(\d+)', fold).groups()
                      for fold in folds]]

def fold(coords, axis, pos):
  '''Get all coords whose 'axis' value > pos, mirror them in pos,
     then merge them back with the other half of the coords.'''
  to_mirror = set(filter(lambda c: c[axis] > pos, coords))
  mirrored = set((c[0] if axis == 1 else 2 * pos - c[0],
                  c[1] if axis == 0 else 2 * pos - c[1])
                 for c in to_mirror)
  return (coords - to_mirror) | mirrored

print('part 1:', len(fold(coords, *folds[0])))

def draw(coords):
  w, h = max(x for x,_ in coords) + 1, max(y for _,y in coords) + 1
  print(''.join(['-'] * w))
  for y in range(h):
    print(''.join('█' if (x,y) in coords else ' ' for x in range(w)))
  print(''.join(['-'] * w))

print('part 2:')
draw(reduce(lambda c,f: fold(c, *f), folds, coords))

