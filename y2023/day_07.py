from collections import Counter
from time import perf_counter

def parse_data(filename):
  # "KK677 28" becomes: ([13,13,6,7,7], 28)
  letter_card_ranks = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
  data = [(list(hand), int(bid)) for hand, bid in map(str.split, open(filename).readlines())]
  return [([int(h) if h.isdigit() else letter_card_ranks[h] for h in hand], bid) for hand,bid in data]

st = perf_counter()
data = parse_data('day_07_input.txt')
parse_time = 1000 * (perf_counter() - st)
test_data = parse_data('day_07_test_input.txt')

def rank(hand):
  # Returns a tuple: (hand type, hand[0][0], hand[0][1], ...)
  c = Counter(hand[0])
  max_card_frequency = max(c.values())
  num_unique_cards = len(c)
  num_jokers = c[1]
  if num_unique_cards == 1:
    hand_type = 7  # five of a kind
  elif max_card_frequency == 4:
    if num_jokers > 0:
      hand_type = 7  # can be promoted to 5 of a kind (JJJJx or xxxxJ)
    else:
      hand_type = 6  # four of a kind
  elif max_card_frequency == 3:
    if num_unique_cards == 2:
      if num_jokers > 0:
        hand_type = 7  # can be promoted to 5 of a kind (JJJxx or xxxJJ)
      else:
        hand_type = 5  # full house
    else:
      if num_jokers > 0:
        hand_type = 6  # can be promoted to 4 of a kind (JJJxy or xxxJy)
      else:
        hand_type = 4  # three of a kind
  elif max_card_frequency == 2:
    if num_unique_cards == 3:
      if num_jokers == 2:
        hand_type = 6  # can be promoted to 4 of a kind (JJxxy)
      elif num_jokers == 1:
        hand_type = 5  # can be promoted to a full house (Jxxyy)
      else:
        hand_type = 3  # two pair
    else:
      if num_jokers > 0:
        hand_type = 4  # can be promoted to 3 of a kind (JJxyz or Jxxyz)
      else:
        hand_type = 2  # one pair
  elif num_jokers == 1:
    hand_type = 2  # can be promoted to one pair (Jxyzw)
  else:
    hand_type = 1  # high card
  return tuple([hand_type] + hand[0])

def part1(test=False):
  hands = test_data if test else data
  return sum(bid * (idx + 1) for idx, (_, bid) in enumerate(sorted(hands, key=rank)))

def part2(test=False):
  hands = test_data if test else data
  # Convert all the 11's (Jacks) to 1's (Jokers)
  hands = [([1 if c == 11 else c for c in hand], bid) for hand,bid in hands]
  return sum(bid * (idx + 1) for idx, (_, bid) in enumerate(sorted(hands, key=rank)))

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  st = perf_counter()
  p1 = part1()
  p1_time = 1000 * (perf_counter() - st)
  st = perf_counter()
  p2 = part2()
  p2_time = 1000 * (perf_counter() - st)
  print('Data parse:', f'{parse_time:.4} ms')
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 6440 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 5905 else '(failed)')
  print('Part 1:', p1, f'({p1_time:.4} ms)')
  print('Part 2:', p2, f'({p2_time:.4} ms)')
