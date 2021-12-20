from math import cos, sin
import numpy as np
import re

def rotate(vector, amount):
  theta = np.radians(amount)
  return map(lambda x: int(round(x)), np.dot(vector, np.array([[cos(theta), -sin(theta)], [sin(theta), cos(theta)]])))

commands_pt1 = {
  'N': lambda pos, dirn, arg: (np.add(pos, (0, arg)), dirn),
  'S': lambda pos, dirn, arg: (np.add(pos, (0, -arg)), dirn),
  'E': lambda pos, dirn, arg: (np.add(pos, (arg, 0)), dirn),
  'W': lambda pos, dirn, arg: (np.add(pos, (-arg, 0)), dirn),
  'F': lambda pos, dirn, arg: (np.add(pos, np.multiply(dirn, arg)), dirn),
  'L': lambda pos, dirn, arg: (pos, rotate(dirn, -arg)),
  'R': lambda pos, dirn, arg: (pos, rotate(dirn, arg))
}

commands_pt2 = {
  'N': lambda pos, wayp, arg: (pos, np.add(wayp, (0, arg))),
  'S': lambda pos, wayp, arg: (pos, np.add(wayp, (0, -arg))),
  'E': lambda pos, wayp, arg: (pos, np.add(wayp, (arg, 0))),
  'W': lambda pos, wayp, arg: (pos, np.add(wayp, (-arg, 0))),
  'F': lambda pos, wayp, arg: (np.add(pos, np.multiply(wayp, arg)), wayp),
  'L': lambda pos, wayp, arg: (pos, rotate(wayp, -arg)),
  'R': lambda pos, wayp, arg: (pos, rotate(wayp, arg))
}

with open('12_input.txt') as f:
  dirs = [re.match(r'^([A-Z])(\d+)', l).groups() for l in f]
print 'part 1: %d' % sum(map(abs, reduce(lambda (p, d), (c, a): commands_pt1[c](p, d, int(a)), dirs, ((0,0), (1,0)))[0]))
print 'part 2: %d' % sum(map(abs, reduce(lambda (p, w), (c, a): commands_pt2[c](p, w, int(a)), dirs, ((0,0), (10,1)))[0]))

