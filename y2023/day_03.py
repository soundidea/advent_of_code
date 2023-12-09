import re

data_files = [
  'day_03_input.txt',
  'day_03_test_input.txt'
]

symbol_parser = re.compile(r'[^\d.]')
part_parser = re.compile(r'\d+')

def parse_data(filename):
  schematic = list(map(str.strip, open(filename).readlines()))
  symbols = [{m.start(): m.group(0) for m in symbol_parser.finditer(l)} for l in schematic]
  parts = [{m.span(): int(m.group(0)) for m in part_parser.finditer(l)} for l in schematic]
  return (symbols, parts)

def part_touches_any_symbols(row, part, symbol_positions):
  (x1,x2),_ = part
  r = set(range(x1-1, x2+1))
  return ((len(symbol_positions[row-1] & r) if row > 0 else False) or
          len(symbol_positions[row] & r) or
          (len(symbol_positions[row+1] & r) if row < len(symbol_positions)-1 else False))

def parts_touching_pos(row, col, parts):
  return [p for r in range(row-1,row+2) 
            for p in parts[r].items()
            if p[0][0]-1 <= col <= p[0][1]]

def part1(data):
  symbols, parts = data
  symbol_positions = [set(ss.keys()) for ss in symbols]
  return sum(part[1]
             for row,pp in enumerate(parts)
             for part in pp.items()
             if part_touches_any_symbols(row, part, symbol_positions))

def part2(data):
  symbols, parts = data
  gear_ratios = []
  for row,ss in enumerate(symbols):
    for col,s in ss.items():
      if s=='*':
        pp = parts_touching_pos(row, col, parts)
        if 2 == len(pp):
          gear_ratios.append(pp[0][1] * pp[1][1])
  return sum(gear_ratios)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 4361 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 467835 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)

