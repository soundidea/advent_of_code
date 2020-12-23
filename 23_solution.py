def play_game(cups, turns):
  cur = cups[0]
  num_cups = len(cups)
  cups = dict(zip(cups, cups[1:] + cups[:1]))
  for _ in range(turns):
    to_move = [cups[cur], cups[cups[cur]], cups[cups[cups[cur]]]]
    dest = cur
    while dest == cur or dest in to_move:
      dest = ((dest - 2) % num_cups) + 1
    cups[cur] = cups[to_move[-1]]
    cups[to_move[-1]] = cups[dest]
    cups[dest] = to_move[0]
    cur = cups[cur]
  return cups

my_input = [6,1,4,7,5,2,8,3,9]
cups_1 = play_game(my_input, 100)
cups_2 = play_game(my_input + range(10,1000001), 10000000)
print 'part 1:', ''.join(map(str, reduce(lambda c,_: c + [cups_1[c[-1]]], range(len(my_input)-2), [cups_1[1]])))
print 'part 2:', cups_2[1] * cups_2[cups_2[1]]
