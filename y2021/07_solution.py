def naive_cost(pos, crabs):
  return sum(abs(c - pos) for c in crabs)

def real_cost(pos, crabs):
  return sum(int(abs(c - pos) * (abs(c - pos) + 1) / 2) for c in crabs)

crabs = list(map(int, open('07_input.txt').read().strip().split(',')))
possible_positions = range(min(crabs), max(crabs) + 1)
print('part 1:', min(naive_cost(pos, crabs) for pos in possible_positions))
print('part 2:', min(real_cost(pos, crabs) for pos in possible_positions))
