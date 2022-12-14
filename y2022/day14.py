from copy import deepcopy

def sign(x):
  return (x > 0) - (x < 0)

def cells_between(node1, node2):
  delta = node2 - node1
  step = complex(sign(delta.real), sign(delta.imag))
  yield node1
  while node1 != node2:
    node1 += step
    yield node1

def drop_one_sand(grid, floor):
  s = 500 + 0j
  while s.imag < floor:
    if s + 1j not in grid:
      s += 1j
    elif s + -1+1j not in grid:
      s += -1+1j
    elif s + 1+1j not in grid:
      s += 1+1j
    else:
      break
  return s

def pour_sand(grid, y_stop, floor):
  num_sand = 0
  while (True):
    s = drop_one_sand(grid, floor)
    if s.imag == y_stop:
      break
    grid[s] = 'o'
    num_sand += 1
  return num_sand

lines = [[complex(*map(int, node.split(','))) for node in line.split(' -> ')]
         for line in open('day14_input.txt')
                     .read().strip().split('\n')]
floor = max(int(node.imag) for line in lines for node in line) + 1
grid = {cell: '#' for line in lines
                  for pair in zip(line[:-1], line[1:])
                  for cell in cells_between(pair[0], pair[1])}

print('part 1:', pour_sand(deepcopy(grid), floor, floor))
print('part 2:', pour_sand(grid, 0, floor) + 1)
