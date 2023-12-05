
def parse_data(filename):
  # "Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53"
  # becomes: ({41, 48, 83, 86, 17}, {83, 86, 6, 31, 17, 9, 48, 53})
  cards = map(str.strip, open(filename).readlines())
  cards = [tuple(set(map(int, g.split()))
                 for g in c.split(': ')[1].split(' | '))
           for c in cards]
  return cards

cards = parse_data('day_04_input.txt')
test_cards = parse_data('day_04_test_input.txt')

def part1(test=False):
  return sum(0 if not len(c[1] & c[0])
             else 2**(len(c[1] & c[0])-1)
             for c in (test_cards if test else cards))

def part2(test=False):
  data = test_cards if test else cards
  card_counts = [1] * len(data)
  for i,c in enumerate(data):
    matches = len(c[1] & c[0])
    for j in range(i+1, i+1+matches):
      card_counts[j] += card_counts[i]
  return sum(card_counts)
  
if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 13 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 30 else '(failed)')
  print('Part 1:', part1())
  print('Part 2:', part2())

