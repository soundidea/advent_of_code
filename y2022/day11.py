from copy import deepcopy
from dataclasses import dataclass, field
from math import prod

@dataclass
class Monkey:
  op: 'typing.Any'
  div: int
  dest_t: int
  dest_f: int
  items: list = field(default_factory=list)

  def __init__(self, lines, num):
    self.items = [int(i) for i in lines[1][18:].split(', ')]
    self.op = compile(lines[2][19:], 'monkey%d' % num, 'eval')
    self.div = int(lines[3][21:])
    self.dest_t = int(lines[4][29:])
    self.dest_f = int(lines[5][30:])

def run_game(num_rounds, monkeys, div_three=True):
  group = prod(m.div for m in monkeys)
  num_inspections = [0 for _ in range(len(monkeys))]
  for _ in range(num_rounds):
    for i, m in enumerate(monkeys):
      num_inspections[i] += len(m.items)
      for item in m.items:
        item = eval(m.op, {'old': item})
        if (div_three):
          item //= 3
        else:
          item %= group
        dest = m.dest_t if (0 == (item % m.div)) else m.dest_f
        monkeys[dest].items.append(item)
      m.items.clear()
  return prod(sorted(num_inspections, reverse=True)[:2])

monkeys = [Monkey(m.split('\n'), i) for i,m in enumerate(open('day11_input.txt').read().split('\n\n'))]
print(run_game(20, deepcopy(monkeys)))
print(run_game(10000, monkeys, div_three=False))
