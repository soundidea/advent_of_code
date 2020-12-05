
def sum_to(n):
  return n * (n+1) / 2


if __name__ == '__main__':
  with open('5_input.txt') as f:
      seats = [8 * int(p[:7].replace('F', '0').replace('B', '1'), 2)
                 + int(p[7:10].replace('R', '1').replace('L', '0'), 2)
               for p in f.readlines()]
  print 'part 1: %d' % max(seats)
  print 'part 2: %d' % (sum_to(max(seats)) - sum_to(min(seats)-1) - sum(seats))
