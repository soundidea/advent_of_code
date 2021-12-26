from itertools import count, product
from collections import Counter, defaultdict

def play_games(games, dice, winning_score):
  turn = 0
  won_games = defaultdict(int)
  while len(games):
    updated_games = defaultdict(int)
    for (p1,p2), freq in games.items():
      for throw, throw_freq in next(dice).items():
        pos, score = (p2 if (turn%2) else p1)
        pos = ((pos + throw - 1) % 10) + 1
        score += pos
        new_state = (p1, (pos, score)) if (turn%2) else ((pos, score), p2)
        if score >= winning_score:
          won_games[new_state] += freq * throw_freq
        else:
          updated_games[new_state] += freq * throw_freq
    games = updated_games
    turn += 1
  return turn, won_games

def deterministic_dice():
  c = count()
  while True:
    yield {sum(1 + next(c) % 100 for _ in range(3)): 1}

def dirac_dice():
  # With 3 throws of a Dirac die there are 7 possible outcomes: 3,4,5,6,7,8,9
  # dirac_throws counts how many ways you could get each of them.
  # There are 27 permutations of dice throws, and sum(dirac_throws.values()) == 27
  dirac_throws = Counter(map(sum, product(*[(1,2,3)] * 3)))
  while True:
    yield dirac_throws

# dict of { ( player1 (position, score), player2 ) : num ways to get to this state }
#games = {((4,0), (8,0)): 1}   # test input
games = {((9,0), (10,0)): 1}   # my input

last_turn, won_games = play_games(games, deterministic_dice(), 1000)
print('part 1:', 3 * last_turn * min(s for _,s in list(won_games.keys())[0]))

_, won_games = play_games(games, dirac_dice(), 21)
p1_won = sum(f for ((_,p1),(_,p2)),f in won_games.items() if p1 > p2)
p2_won = sum(f for ((_,p1),(_,p2)),f in won_games.items() if p1 < p2)
print('part 2:', max(p1_won, p2_won))
