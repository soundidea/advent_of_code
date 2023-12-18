from functools import cache

data_files = [
  'day_12_input.txt',
  'day_12_test_input.txt'
]

def parse_data(filename):
  records = map(str.split, map(str.strip, open(filename).readlines()))
  records = [(pattern, tuple(map(int, damaged_blocks.split(','))))
             for pattern, damaged_blocks in records]
  return records

@cache
def count_arrangements(pattern, damaged_blocks):
  if not damaged_blocks:
    return 0 if '#' in pattern else 1
  if not pattern:
    return 1 if not damaged_blocks else 0
  result = 0
  if pattern[0] in ['.', '?']:
    result += count_arrangements(pattern[1:], damaged_blocks)
  if pattern[0] in ['#', '?']:
    block_len = damaged_blocks[0]
    if (block_len <= len(pattern) and
        "." not in pattern[:block_len] and
        (block_len == len(pattern) or
         pattern[block_len] != '#')):
      result += count_arrangements(pattern[block_len + 1:], damaged_blocks[1:])
  return result

def part1(data):
  total = 0
  for pattern, damaged_blocks in data:
    total += count_arrangements(pattern, damaged_blocks)
  return total

def part2(data):
  total = 0
  for pattern, damaged_blocks in data:
    pattern = '?'.join([pattern] * 5)
    damaged_blocks = damaged_blocks * 5
    total += count_arrangements(pattern, damaged_blocks)
  return total

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 21 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 525152 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
