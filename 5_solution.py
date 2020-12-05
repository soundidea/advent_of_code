def sum_to(n):
  return n * (n+1) / 2

if __name__ == '__main__':
  with open('5_input.txt') as f:
    seats = [reduce(lambda a, b: a * 2 + (1 if b in ['B','R'] else 0), l[:10], 0) for l in f.readlines()]
  print 'part 1: %d' % max(seats)
  print 'part 2: %d' % (sum_to(max(seats)) - sum_to(min(seats)-1) - sum(seats))
