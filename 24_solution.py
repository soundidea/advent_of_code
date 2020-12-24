import re
from collections import Counter
from itertools import chain

# Represent the hex grid as a skewed rectangular grid.
# See: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
do_move = {
  'e': lambda (x,y): (x+1,y),
  'w': lambda (x,y): (x-1,y),
  'ne': lambda (x,y): (x+1,y+1),
  'nw': lambda (x,y): (x,y+1),
  'se': lambda (x,y): (x,y-1),
  'sw': lambda (x,y): (x-1,y-1),
}

def neighbours((x,y), include_center=False):
  if include_center: return [(x,y), (x+1,y), (x-1,y), (x+1,y+1), (x,y+1), (x,y-1), (x-1,y-1)]
  else:              return [(x+1,y), (x-1,y), (x+1,y+1), (x,y+1), (x,y-1), (x-1,y-1)]

def evolve_floor(black_tiles, num_days):
  for _ in range(num_days):
    candidates = set(chain.from_iterable(neighbours(t,True) for t in black_tiles))
    new_day = []
    for tile in candidates:
      num_black_neighbours = sum(1 for n in neighbours(tile) if n in black_tiles)
      if ((tile in black_tiles and 1 <= num_black_neighbours <= 2)
          or (tile not in black_tiles and num_black_neighbours == 2)):
        new_day.append(tile)
    black_tiles = new_day
  return black_tiles

flip_tiles = [re.findall(r'(se|sw|ne|nw|e|w)', l) for l in open('24_input.txt')]
flip_tiles = [reduce(lambda c,d: do_move[d](c), moves, (0,0)) for moves in flip_tiles]
black_tiles = [coord for (coord, num_flips) in Counter(flip_tiles).items() if (num_flips % 2)]
print 'part 1:', len(black_tiles)
print 'part 2:', len(evolve_floor(black_tiles, 100))
