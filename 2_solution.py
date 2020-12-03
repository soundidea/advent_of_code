import re

if __name__ == '__main__':
  with open('2_input.txt') as f:
    passwords = [re.match(r'(\d+)-(\d+) ([a-z]): (\w+)', line).groups() for line in f.readlines()]
  passwords = [(int(p[0]), int(p[1]), p[2], p[3]) for p in passwords]
  print 'part 1: %d' % sum(1 for p in passwords if p[0] <= p[3].count(p[2]) <= p[1])
  print 'part 2: %d' % sum(1 for p in passwords if (p[3][p[0]-1] == p[2]) ^ (p[3][p[1]-1] == p[2]))
