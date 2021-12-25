from itertools import count

i = list(map(str.strip, open('25_input.txt').readlines()))
w, h = len(i[0]), len(i)
cucumbers = {(x,y): c for y,row in enumerate(i) for x,c in enumerate(row) if c != '.'}
stages = [('>', lambda x,y: ((x+1)%w, y)),
          ('v', lambda x,y: (x, (y+1)%h))]
for step in count(1):
  num_moves = 0
  for herd, mv in stages:
    new_c = dict([(mv(x,y), c) if c == herd and mv(x,y) not in cucumbers
                               else ((x,y),c)
                  for (x,y),c in cucumbers.items()])
    num_moves += len(set(new_c.keys()) - set(cucumbers.keys()))
    cucumbers = new_c
  if not num_moves:
    print('part 1', step)
    break
    
