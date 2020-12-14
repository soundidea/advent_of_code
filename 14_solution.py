from itertools import compress, product
import re

with open('14_input.txt') as f:
  program = [(re.match(r'(mem)\[(\d+)\] = (\d+)', l) or re.match(r'(mask) = ([01X]+)', l)).groups() for l in f]
  program = [(c[0], None, c[1]) if c[0] == 'mask' else (c[0], int(c[1]), int(c[2])) for c in program]

masks, mem_pt1, mem_pt2 = {}, {}, {}
for instr, addr, arg in program:
  if instr == 'mask':
    masks = {d: reduce(lambda a, b: a * 2 + (1 if b == d else 0), arg, 0) for d in ('0', '1')}
    masks.update({'X': [2**(35-idx) for idx, bit in enumerate(arg) if bit == 'X']})
  else:
    mem_pt1[addr] = (arg | masks['1']) & ~masks['0']
    for sel in product((0, 1), repeat=len(masks['X'])):
      on, off = (sum(compress(masks['X'], sel)) | masks['1'],
                 sum(compress(masks['X'], map(lambda s: 1-s, sel))))
      mem_pt2[(addr | on) & ~off] = arg
    
print 'part 1: %d' % sum(mem_pt1.values())
print 'part 2: %d' % sum(mem_pt2.values())

