
if __name__ == '__main__':
  with open('6_input.txt') as f:
    groups = [[set(p) for p in g.rstrip().split('\n')] for g in f.read().split('\n\n')]
  print 'part 1: %d' % sum(len(reduce(lambda a, b: a.union(b), g)) for g in groups)
  print 'part 2: %d' % sum(len(reduce(lambda a, b: a.intersection(b), g)) for g in groups)
