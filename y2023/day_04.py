data_files = [
  # Add a 3rd entry if part 2 needs different test data.
  'day_04_input.txt',
  'day_04_test_input.txt'
]

def parse_data(filename):
  # "Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53"
  # becomes: ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})
  cards = map(str.strip, open(filename).readlines())
  cards = [tuple(set(map(int, g.split()))
                 for g in c.split(': ')[1].split(' | '))
           for c in cards]
  return cards

def part1(cards):
  return sum(0 if not len(c[1] & c[0])
             else 2**(len(c[1] & c[0])-1)
             for c in cards)

def part2(cards):
  card_counts = [1] * len(cards)
  for i,c in enumerate(cards):
    matches = len(c[1] & c[0])
    for j in range(i+1, i+1+matches):
      card_counts[j] += card_counts[i]
  return sum(card_counts)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 13 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 30 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
