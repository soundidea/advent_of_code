from itertools import repeat

def parse_data(filename):
  f = open(filename).read().strip().split('\n\n')
  seeds = list(map(int, f[0].split(': ')[1].split()))
  span_maps = [[list(map(int, line.split())) for line in m.split('\n')[1:]] for m in f[1:]]
  span_maps = [sorted((line[1], line[2], line[0]) for line in m) for m in span_maps]
  # Fill any gaps in the map ranges...
  for m in span_maps:
    pos = 0
    for i, rng in enumerate(m):
      if rng[0] > pos:
        m.insert(i, (pos, rng[0] - pos, pos))
      pos += m[i][1]
  return (seeds, span_maps)

data = parse_data('day_05_input.txt')
test_data = parse_data('day_05_test_input.txt')

def map_range(seed_rng, span_map):
  result = []
  pos, end = seed_rng[0], sum(seed_rng)
  for span_start, span_len, dest_start in span_map:
    if span_start + span_len < pos:
      continue
    dist = pos - span_start
    result.append((dest_start + dist, min(span_len - dist, end-pos)))
    pos = span_start + span_len
    if pos >= end:
      break
  if pos < end:
    result.append((pos, end-pos))
  return result

def do_run(seed_ranges, maps):
  for span_map in maps:
    new_ranges = []
    for r in seed_ranges:
      new_ranges.extend(map_range(r, span_map))
    seed_ranges = new_ranges
  return min(seed_ranges)[0]

def part1(test=False):
  seeds, maps = test_data if test else data
  # Do the run with ranges [(seeds[0], 1), (seeds[1], 1), ...]
  return do_run(zip(seeds, repeat(1)), maps)

def part2(test=False):
  seeds, maps = test_data if test else data
  # Do the run with ranges [(seeds[0], seeds[1]), (seeds[2], seeds[3]), ...]
  return do_run(zip(seeds[:-1:2], seeds[1::2]), maps)

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 35 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 46 else '(failed)')
  print('Part 1:', part1())
  print('Part 2:', part2())
