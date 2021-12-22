from itertools import dropwhile, product
from math import ceil, sqrt
import re

def final_pos(x_vel, y_vel, t_left, t_top):
  '''Given an initial velocity (x_vel, y_vel) calculate where the probe
     will be when it passes the top left of the target zone.'''
  b = (2 * x_vel + 1) / 2
  xt = int(ceil(b - sqrt(b**2 - 2 * t_left)))
  b = (2 * y_vel + 1) / 2
  yt = int(ceil(b + sqrt(b**2 - 2 * t_top)))
  t = max(xt, yt)
  xt = min(x_vel, t)
  return ((2 * x_vel + 1 - xt) * xt // 2, (2 * y_vel + 1 - t) * t // 2)

target = list(map(int, re.search(r'target area: x=([-\d]+)..([-\d]+), y=([-\d]+)..([-\d]+)',
                                 open('17_input.txt').read()).groups()))

t_left, t_right = sorted(target[:2])
t_bottom, t_top = sorted(target[2:])

y_vels = range(t_bottom, -t_bottom)
x_vels = range(int(ceil(sqrt(2 * t_left + 0.25) - 0.5)), t_right + 1)
target_zone = set(product(range(t_left, t_right + 1), range(t_bottom, t_top + 1)))

print('part 1:', t_bottom * (t_bottom+1) // 2)
print('part 2:', sum(final_pos(*init_velocity, t_left, t_top) in target_zone
                     for init_velocity in product(x_vels, y_vels)))

