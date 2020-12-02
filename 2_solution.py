import re
from collections import Counter


if __name__ == '__main__':
  with open('2_input.txt') as f:
    passwords = [re.match(r'(\d+)-(\d+) ([a-z]): (\w+)', line).groups() for line in f.readlines()]
  passwords = [(int(p[0]), int(p[1]), p[2], p[3]) for p in passwords]
  print 'part 1: %d' % len(filter(lambda p: p[0] <= Counter(p[3])[p[2]] <= p[1], passwords))
  print 'part 2: %d' % len(filter(lambda p: Counter((p[3][p[0]-1], p[3][p[1]-1]))[p[2]] == 1, passwords))
