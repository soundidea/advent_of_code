from a_star import a_star

squares = {complex(x,y): h
           for y,row in enumerate(open('day12_input.txt')
                                  .read().strip().split('\n'))
           for x,h in enumerate(row)}
S = next(filter(lambda s: s[1] == 'S', squares.items()))[0]
E = next(filter(lambda s: s[1] == 'E', squares.items()))[0]
squares[S] = 'a'
squares[E] = 'z'
squares = {s[0]: ord(s[1]) - ord('a') for s in squares.items()}

# Starting at S, stop when you reach E. The heuristic is 26 minus the value
# of the square (i.e. I am 5 moves away if my current square height is 21).
# The neighbours are the ones that can be reached when walking uphill. The
# edge weight is just 1 (i.e. no weights).
print('part 1:',
      len(a_star(S,
                 lambda pos: pos == E,
                 lambda pos: 26 - squares[pos],
                 lambda pos: filter(lambda p: p in squares and
                                              squares[p] <= squares[pos] + 1,
                                    [pos+d for d in (1,-1,1j,-1j)]),
                 lambda pos, neighbour: 1)) - 1)

# Starting at E, stop when you hit a square with value 0 ('a'). The
# heuristic is just the value of the square (i.e. I am 5 moves away if my
# current square height is 5). The neighbours are the ones where you could
# walk from them to pos. The edge weight is just 1 (i.e. no weights).
print('part 2:',
      len(a_star(E,
                 lambda pos: squares[pos] == 0,
                 lambda pos: squares[pos],
                 lambda pos: filter(lambda p: p in squares and
                                              squares[p] >= squares[pos] - 1,
                                    [pos+d for d in (1,-1,1j,-1j)]),
                 lambda pos, neighbour: 1)) - 1)
