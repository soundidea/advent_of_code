import re
from collections import Counter

# Represent the hex grid as a skewed rectangular grid.
# See: https://www.redblobgames.com/grids/hexagons/#coordinates-axial
directions = {
  'e': 1 + 0j,
  'w': -1 + 0j,
  'ne': 1 + 1j,
  'nw': 0 + 1j,
  'se': 0 - 1j,
  'sw': -1 - 1j
}
offsets = directions.values()

def evolve_floor(black_tiles, num_days):
  for _ in range(num_days):
    candidates = black_tiles.union(t + offset for t in black_tiles for offset in offsets)
    next_day = set()
    for tile in candidates:
      blk_n = sum(tile + offset in black_tiles for offset in offsets)
      if (tile in black_tiles and 1 <= blk_n <= 2) or (tile not in black_tiles and blk_n == 2):
        next_day.add(tile)
    black_tiles = next_day
  return black_tiles

flip_tiles = [re.findall(r'(se|sw|ne|nw|e|w)', l) for l in open('24_input.txt')]
flip_tiles = [reduce(lambda coord, move: coord + directions[move], moves, 0 + 0j) for moves in flip_tiles]
black_tiles = {coord for (coord, num_flips) in Counter(flip_tiles).items() if (num_flips % 2)}
print 'part 1:', len(black_tiles)
print 'part 2:', len(evolve_floor(black_tiles, 100))
