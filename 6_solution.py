
if __name__ == '__main__':
  with open('6_input.txt') as f:
    groups = [g.rstrip().split('\n') for g in f.read().split('\n\n')]

  print 'part 1: %d' % sum(len(reduce(lambda a, b: set(a).union(set(b)), g)) for g in groups)
  print 'part 2: %d' % sum(len(reduce(lambda a, b: set(a).intersection(set(b)), g)) for g in groups)
