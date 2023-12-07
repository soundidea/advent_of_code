from collections import Counter

def parse_data(filename):
  letter_card_ranks = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
  data = [(list(hand), int(bid)) for hand, bid in map(str.split, open(filename).readlines())]
  return [([int(h) if h.isdigit() else letter_card_ranks[h] for h in hand], bid) for hand,bid in data]

data = parse_data('day_07_input.txt')
test_data = parse_data('day_07_test_input.txt')

def type_rank(hand):
  c = Counter(hand)
  max_v, l, num_jokers = max(c.values()), len(c), c[1]
  if l == 1:
    return 7  # five of a kind
  if max_v == 4:
    if num_jokers > 0:
      return 7  # can be promoted to 5 of a kind (JJJJx or xxxxJ)
    return 6  # four of a kind
  if max_v == 3:
    if min(c.values()) == 2:
      if num_jokers > 0:
        return 7  # can be promoted to 5 of a kind (JJJxx or xxxJJ)
      return 5  # full house
    else:
      if num_jokers > 0:
        return 6  # can be promoted to 4 of a kind (JJJxy or xxxJy)
      return 4  # three of a kind
  if max_v == 2:
    if l == 3:
      if num_jokers == 2:
        return 6  # can be promoted to 4 of a kind (JJxxy)
      if num_jokers == 1:
        return 5  # can be promoted to a full house (Jxxyy)
      return 3  # two pair
    else:
      if num_jokers > 0:
        return 4  # can be promoted to 3 of a kind (JJxyz or Jxxyz)
      return 2  # one pair
  if num_jokers == 1:
    return 2  # can be promoted to one pair (Jxyzw)
  return 1  # high card

def cmp(hand):
  hand = hand[0]
  key = type_rank(hand)
  for card in hand:
    key = 15 * key + card
  return key

def part1(test=False):
  hands = test_data if test else data
  return sum(bid * (idx + 1) for idx, (_, bid) in enumerate(sorted(hands, key=cmp)))

def part2(test=False):
  hands = test_data if test else data
  # Convert all the 11's (Jacks) to 1's (Jokers)
  hands = [([1 if c == 11 else c for c in hand], bid) for hand,bid in hands]
  return sum(bid * (idx + 1) for idx, (_, bid) in enumerate(sorted(hands, key=cmp)))

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 6440 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 5905 else '(failed)')
  print('Part 1:', part1())
  print('Part 2:', part2())
