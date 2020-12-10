from itertools import combinations

def sublist_summing_to(expenses, length, value):
  return next(c for c in combinations(expenses, length) if sum(c) == value)

# In Python3 this isn't needed, just use math.prod().
def product(values):
  return reduce(lambda a, b: a * b, values)

with open('01_input.txt') as f:
  expenses = list(map(int, f))
print 'part 1: %d' % product(sublist_summing_to(expenses, 2, 2020))
print 'part 2: %d' % product(sublist_summing_to(expenses, 3, 2020))
