def play_game(cups, turns):
  cur = cups[0]
  num_cups = len(cups)
  cups = dict(zip(cups, cups[1:] + cups[:1]))
  for _ in range(1, turns + 1):
    to_move = [cups[cur], cups[cups[cur]], cups[cups[cups[cur]]]]
    dest = cur
    while dest == cur or dest in to_move:
      dest = ((dest - 2) % num_cups) + 1
    cups[cur] = cups[to_move[-1]]
    cups[to_move[-1]] = cups[dest]
    cups[dest] = to_move[0]
    cur = cups[cur]
  return cups

cups = play_game([6,1,4,7,5,2,8,3,9], 100)
print 'part 1:', ''.join(map(str, reduce(lambda c,_: c + [cups[c[-1]]], range(len(cups)-2), [cups[1]])))

cups = play_game([6,1,4,7,5,2,8,3,9] + range(10,1000001), 10000000)
print 'part 2:', cups[1] * cups[cups[1]]
