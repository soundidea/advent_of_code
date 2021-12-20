from collections import Counter
from itertools import chain, count, izip, takewhile
import re

def covered_cells(lines):
  '''Returns the cells covered by all the lines. Repeats occur if lines cross.'''
  return chain.from_iterable(takewhile(lambda coord: coord != (l[2] + cmp(l[2], l[0]),
                                                               l[3] + cmp(l[3], l[1])),
                                       izip(count(l[0], cmp(l[2], l[0])),
                                            count(l[1], cmp(l[3], l[1]))))
                             for l in lines)

lines = [map(int, re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line).groups())
         for line in open('05_input.txt').readlines()]
h_or_v = filter(lambda l: l[0] == l[2] or l[1] == l[3], lines)
print 'part 1:', sum(n > 1 for (_,n) in Counter(covered_cells(h_or_v)).iteritems())
print 'part 2:', sum(n > 1 for (_,n) in Counter(covered_cells(lines)).iteritems())
