import re

input_re = re.compile(r'(\d+)-(\d+) ([a-z]): (\w+)')

with open('02_input.txt') as f:
  passwords = [input_re.match(l).groups() for l in f]
  passwords = [(int(p[0]), int(p[1]), p[2], p[3]) for p in passwords]
print 'part 1: %d' % sum(1 for p in passwords if p[0] <= p[3].count(p[2]) <= p[1])
print 'part 2: %d' % sum(1 for p in passwords if (p[3][p[0]-1] == p[2]) ^ (p[3][p[1]-1] == p[2]))
