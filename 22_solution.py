def play_combat(p1,p2):
  while len(p1) and len(p2):
    c1,c2 = p1[0], p2[0]
    p1 = p1[1:] + ([c1,c2] if c1>c2 else [])
    p2 = p2[1:] + ([c2,c1] if c2>c1 else [])
  return p1 if len(p1) else p2

def play_recursive_combat(p1,p2):
  seen_hands = set()
  while len(p1) and len(p2):
    this_hand = str(p1) + str(p2)
    if this_hand in seen_hands:
      return 1,p1
    seen_hands.add(this_hand)
    c1,c2,p1,p2 = p1[0], p2[0], p1[1:], p2[1:]
    if len(p1) >= c1 and len(p2) >= c2:
      winner,_ = play_recursive_combat(p1[:c1], p2[:c2])
    else:
      winner = 1 if c1 > c2 else 2
    p1 += ([c1,c2] if winner == 1 else [])
    p2 += ([c2,c1] if winner == 2 else [])
  winner = (1,p1) if len(p1) else (2,p2)
  return winner

hands = [map(int, p.splitlines()[1:]) for p in open('22_input.txt').read().split('\n\n')]
print 'part 1:', sum(i*c for i,c in enumerate(play_combat(*hands)[::-1], 1))
print 'part 2:', sum(i*c for i,c in enumerate(play_recursive_combat(*hands)[1][::-1], 1))

