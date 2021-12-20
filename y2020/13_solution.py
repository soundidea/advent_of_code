from itertools import count
from operator import mul

with open('13_input.txt') as f:
  timestamp, buses = [l.strip() for l in f]
  buses = sorted([(int(bus), idx) for idx, bus in enumerate(buses.split(',')) if bus != 'x'], reverse=True)
  # with the test input, buses = [(59, 4), (31, 6), (19, 7), (13, 1), (7, 0)]

print 'part 1: %d' % reduce(mul, min((bus - (int(timestamp) % bus), bus) for bus,_ in buses))
print 'part 2: %d' % reduce(lambda (t, step), (bus, offs): next((c, step * bus) for c in count(t, step) if (c + offs) % bus == 0), buses, (0, 1))[0]


# Slightly more readable version of part 2 (same algorithm):
t, step = 0, 1
for bus, offs in buses:
  for c in count(t, step):
    if (c + offs) % bus == 0:
      t, step = c, step * bus
      break
print 'part 2: %d' % t
