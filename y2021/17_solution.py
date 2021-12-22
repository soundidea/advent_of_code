from itertools import dropwhile, product
from math import ceil, sqrt
import re

def next_pos(initial_velocity):
  pos, vel = (0,0), initial_velocity
  while True:
    pos = (pos[0] + vel[0], pos[1] + vel[1])
    vel = (max(0, vel[0] - 1), vel[1] - 1)
    yield pos

target = list(map(int, re.search(r'target area: x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)',
                                 open('17_input.txt').read()).groups()))

t_left, t_right = sorted(target[:2])
t_bottom, t_top = sorted(target[2:])

y_vels = range(t_bottom, -t_bottom)
x_vels = range(int(ceil(sqrt(2 * t_left + 0.25) - 0.5)), t_right + 1)
target_zone = set(product(range(t_left, t_right + 1), range(t_bottom, t_top + 1)))

print('part 1:', t_bottom * (t_bottom+1) // 2)
print('part 2:', sum(next(dropwhile(lambda pos: pos[0] < t_left or pos[1] > t_top,
                                    next_pos(u)))
                     in target_zone
                     for u in product(x_vels, y_vels)))

