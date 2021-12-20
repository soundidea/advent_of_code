def play_game(cups, turns):
  cur = cups[0]-1
  # Each cup is the index of the next, with all the cup labels subtracted by 1 to make it all zero-based
  # So the example input '389125467' becomes [1,4,7,5,3,6,2,8,0], i.e. cup 3 (index 2) points to index 7 (cup 8)
  cups = map(lambda (_,b): b-1, sorted(zip(cups, cups[1:] + cups[:1])))
  num_cups = len(cups)
  for _ in range(turns):
    to_move = [cups[cur], cups[cups[cur]], cups[cups[cups[cur]]]]
    dest = (cur - 1) % num_cups
    while dest in to_move:
      dest = (dest - 1) % num_cups
    cups[cur] = cups[to_move[-1]]
    cups[to_move[-1]] ] = cups[dest]
    cups[dest] = to_move[0]
    cur = cups[cur]
  return cups

my_input = [6,1,4,7,5,2,8,3,9]
cups_1 = play_game(my_input, 100)
cups_2 = play_game(my_input + range(10,1000001), 10000000)
print 'part 1:', ''.join(map(lambda c: str(c+1), reduce(lambda c,_: c + [cups_1[c[-1]]], range(len(my_input)-2), [cups_1[0]])))
print 'part 2:', (cups_2[0] + 1) * (cups_2[cups_2[0]] + 1)
