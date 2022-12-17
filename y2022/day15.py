import re

def merge(intervals):
  '''Merges the given ranges into as few intervals as possible.

  Args:
      ranges: an iterable of pairs of numbers. Each pair is [min, max)

  Returns:
      A list of number pairs representing the merged ranges.
  '''
  intervals = sorted(intervals, key=lambda x: x[0])
  stack = [list(intervals[0])]
  for i in intervals[1:]:
    if i[0] <= stack[-1][1]:
      stack[-1][1] = max(stack[-1][1], i[1])
    else:
      stack.append(list(i))
  return stack

def intersect(a, b):
  '''Returns the intersection of the two intervals.
     Or the empty list if they don't intersect.'''
  if b[0] >= a[1] or a[0] >= b[1]:
    return []
  return (max(a[0], b[0]), min(a[1], b[1]))

def manhattan(x1, y1, x2, y2):
  return abs(x2-x1) + abs(y2-y1)

def sensor_intervals(sensors, row):
  result = []
  for s in sensors:
    half_width = s[2] - abs(row - s[1])
    if half_width >= 0:
      result.append((s[0] - half_width, s[0] + half_width + 1))
  return result


parser = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')
parsed = [list(map(int, parser.match(line).groups()))
          for line in open('day15_input.txt').read().strip().split('\n')]
sensors = [(p[0], p[1], manhattan(p[0], p[1], p[2], p[3])) for p in parsed]
beacons = set((p[2], p[3]) for p in parsed)

row = 2000000
print('part 1:', sum(i[1] - i[0] for i in merge(sensor_intervals(sensors, row))) -
                 sum(b[1] == row for b in beacons))

# I've seen some really clever solutions that walk around the edges of the
# sensor diamonds and figure out the only possible position of the beacon that
# way, but I'm not smart enough to figure it out for myself, and this runs
# quickly enough, 17 seconds on my laptop.
space_size = 4000001
restrict = (0, space_size)
for y in range(space_size):
  i = [intersect(restrict, i) for i in merge(sensor_intervals(sensors, y))]
  if len(i) > 1:
    print('part 2:', i[0][1] * 4000000 + y)
    break
