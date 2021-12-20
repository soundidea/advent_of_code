from itertools import count

octs = [[int(oc) for oc in row.strip()] for row in open('11_input.txt')]
w,h = len(octs[0]), len(octs)

def flash_inc(octs):
  '''Create a new grid that just counts how many flashes are adjacent to each cell.'''
  return [[sum(octs[yn][xn] >= 10
               for yn in [y-1,y,y+1]
               for xn in [x-1,x,x+1]
               if 0 <= xn < w and 0 <= yn < h)
           for (x,_) in enumerate(row)]
          for (y,row) in enumerate(octs)]

def one_step(octs):
  '''Inc all energy levels by one, then repeatedly 'flash' any >10's by
     setting them to -100 and incrementing their neighbours, until no
     >10s remain. Finally, all the negative cells are flashes, count
     them and set them to 0. Return the tuple: (num flashes, new grid).'''
  to_inc = [[1] * w] * h
  while sum(o for row in to_inc for o in row):
    octs = [[-100 if o >= 10 else o + to_inc[y][x]
             for (x,o) in enumerate(row)]
            for (y,row) in enumerate(octs)]
    to_inc = flash_inc(octs)
  flashes = sum(o < 0 for row in octs for o in row)
  octs = [[max(0, o) for o in row] for row in octs]
  return flashes, octs

total_flashes = 0
for step in count(1):
  n,octs = one_step(octs)
  total_flashes += n
  if step == 100:
    print('part 1:', total_flashes)
  if n == w*h:
    print('part 2:', step)
    break
