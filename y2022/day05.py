import re

def run_moves(stacks, moves, reverse=True):
  stacks = [s[:] for s in stacks]
  for amt, src, dst in moves:
    stacks[src-1], to_move = stacks[src-1][:-amt], stacks[src-1][-amt:]
    stacks[dst-1].extend(to_move[::-1] if reverse else to_move)
  return ''.join(s[-1] for s in stacks)

stacks_in, moves_in = tuple(section.split('\n') for section in open('day05_input.txt').read().split('\n\n'))

stacks = [[] for _ in range(9)]
for line in stacks_in[-2::-1]:
  for pos in range(9):
    if line[1+pos*4].isalnum():
      stacks[pos].append(line[1+pos*4])
moveparser = re.compile(r'^move (\d+) from (\d+) to (\d+)')
moves = [tuple(map(int, moveparser.match(m).groups())) for m in moves_in[:-1]]

print('part 1:', run_moves(stacks, moves))
print('part 2:', run_moves(stacks, moves, reverse=False))

