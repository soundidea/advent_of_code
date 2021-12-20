import re
input = open('04_input.txt').read().split('\n\n')
sequence = map(int, input[0].split(','))
boards = [[map(int, re.findall('\d+', l)) for l in i.strip().split('\n')] for i in input[1:]]

def partition_winners(boards):
  '''Partition the list into winning boards and losing boards.'''
  winners, losers = [], []
  for board in boards:
    transposed = [[row[idx] for row in board] for idx in range(5)]
    (winners if ([None] * 5 in board + transposed) else losers).append(board)
  return winners, losers

winners = []
for n in sequence:
  boards = [[[None if cell == n else cell for cell in row] for row in board] for board in boards]
  wins, boards = partition_winners(boards)
  winners += [(n, board) for board in wins]

print('part 1:', winners[0][0] * sum(cell or 0 for row in winners[0][1] for cell in row))
print('part 2:', winners[-1][0] * sum(cell or 0 for row in winners[-1][1] for cell in row))
