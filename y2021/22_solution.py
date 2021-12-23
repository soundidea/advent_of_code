from functools import reduce
from itertools import product
import re

def intersect(s1, s2):
  def intersect_ranges(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop))
  x_range = intersect_ranges(s1[1], s2[1])
  y_range = intersect_ranges(s1[2], s2[2])
  z_range = intersect_ranges(s1[3], s2[3])
  if len(x_range) and len(y_range) and len(z_range):
    return (-s1[0], x_range, y_range, z_range)
  return False

def step_count_delta(step):
  return step[0] * len(step[1]) * len(step[2]) * len(step[3])

def count_lit_cubes(steps, limit_to_init_region=False):
  '''For each step compare it against all previous ones, if they intersect then
     create a new step that does the opposite of what the other one does (e.g.
     if two steps overlap and they both turn cubes on, then create a new step
     for the overlap which turns those cubes off, so that the final sum for the
     overlap is 1, not 2). Finally, run through the list summing-up the volumes
     of the cuboids, subtracting the ones that turn cubes off.'''
  if (limit_to_init_region):
    init_range = range(-50,51)
    steps = list(filter(lambda s: s,
                        map(lambda s: intersect((-s[0],*[init_range]*3), s), steps)))
  processed = [steps[0]]
  for to_process in steps[1:]:
    for intersect_with in processed.copy():
      new_step = intersect(intersect_with, to_process)
      if new_step:
        processed.append(new_step)
    if to_process[0] > 0:
      processed.append(to_process)
  return sum(map(step_count_delta, processed))

steps = [re.match(
             r'(on|off) x=([-\d]+)..([-\d]+),y=([-\d]+)..([-\d]+),z=([-\d]+)..([-\d]+)',
             line.strip()).groups()
         for line in open('22_input.txt').readlines()]
steps = [(1 if i[0] == 'on' else -1,
           range(int(i[1]), int(i[2]) + 1),
           range(int(i[3]), int(i[4]) + 1),
           range(int(i[5]), int(i[6]) + 1))
          for i in steps]

print('part 1:', count_lit_cubes(steps, limit_to_init_region=True))
print('part 2:', count_lit_cubes(steps))
