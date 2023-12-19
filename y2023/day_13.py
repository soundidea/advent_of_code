data_files = [
  'day_13_input.txt',
  'day_13_test_input.txt'
]

def parse_data(filename):
  grids = open(filename).read().strip().split('\n\n')
  grids = [[[1 if c == '#' else 0 for c in l]
            for l in g.split('\n')] 
           for g in grids]
  return grids

def same_with_smudge(row, other):
  return sum(r != other[i] for i, r in enumerate(row)) == 1

def row_split(grid, part2):
  num_rows = len(grid)
  for idx in range(num_rows - 1):
    i,j, bailed, num_smudges = idx, idx+1, False, 0
    while i >= 0 and j < num_rows:
      identical = (grid[i] == grid[j])
      if part2 and num_smudges == 0 and not identical:
        identical = same_with_smudge(grid[i], grid[j])
        num_smudges += 1
      if not identical:
        bailed = True
        break
      i, j = i - 1, j + 1
    if not bailed and (num_smudges or not part2):
      return idx + 1
  return None

def value(grid, part2=False):
  row = row_split(grid, part2)
  if row:
    return 100 * row
  else:
    w, h = len(grid[0]), len(grid)
    transposed = [[grid[row][col] for row in range(h)] for col in range(w)]
    return row_split(transposed, part2)

def part1(data):
  return sum(value(grid) for grid in data)

def part2(data):
  return sum(value(grid, part2=True) for grid in data)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 405 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 400 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
