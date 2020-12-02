import re
from collections import Counter


if __name__ == '__main__':
  with open('2_input.txt') as f:
    passwords = [re.match(r'(\d+)-(\d+) ([a-z]): (\w+)', line).groups() for line in f.readlines()]
  print 'part 1: %d' % len(filter(lambda p: int(p[0]) <= Counter(p[3])[p[2]] <= int(p[1]), passwords))
  print 'part 2: %d' % len(filter(lambda p: Counter((p[3][int(p[0])-1], p[3][int(p[1])-1]))[p[2]] == 1, passwords))
