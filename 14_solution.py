from collections import defaultdict
from itertools import compress, product
import re

with open('14_input.txt') as f:
  program = [(re.match(r'(mem)\[(\d+)\] = (\d+)', l) or re.match(r'(mask) = ([01X]+)', l)).groups() for l in f]
  program = [(c[0], None, c[1]) if c[0] == 'mask' else (c[0], int(c[1]), int(c[2])) for c in program]


mask_on = 0
mask_off = 0
mem = defaultdict(int)
for instr, addr, arg in program:
  if instr == 'mask':
    mask_on = reduce(lambda a, b: a * 2 + (1 if b == '1' else 0), arg, 0) 
    mask_off = reduce(lambda a, b: a * 2 + (1 if b == '0' else 0), arg, 0) 
  else:
    mem[addr] = (arg | mask_on) & ~mask_off
print 'part 1: %d' % sum(mem.values())


mask_on = 0
mask_float = []
mem = defaultdict(int)
for instr, addr, arg in program:
  if instr == 'mask':
    mask_on = reduce(lambda a, b: a * 2 + (1 if b == '1' else 0), arg, 0) 
    mask_float = [2**(35-idx) for idx, bit in enumerate(arg) if bit == 'X']
  else:
    for sel in product(range(2), repeat=len(mask_float)):
      on = sum(compress(mask_float, sel))
      off = sum(compress(mask_float, map(lambda s: 1-s, sel)))
      mem[(addr | on | mask_on) & ~off] = arg
print 'part 2: %d' % sum(mem.values())
