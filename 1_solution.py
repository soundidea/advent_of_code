from functools import reduce
from itertools import combinations


def list_that_sums_to(expenses, length, value):
  return filter(lambda combo: sum(combo) == value, combinations(expenses, length))[0]


def product(values):
  return reduce(lambda a, b: a * b, values)


if __name__ == '__main__':
  with open('1_input.txt') as f:
    expenses = [int(l.rstrip()) for l in f.readlines()]
  print 'part 1: %d' % product(list_that_sums_to(expenses, 2, 2020))
  print 'part 2: %d' % product(list_that_sums_to(expenses, 3, 2020))

