from itertools import count, product, ifilter, izip, takewhile

def adjacent_seats(seats, part_1, (i, j), (w, h)):
  dirs = filter(lambda d: d != (0,0), product([-1,0,1], repeat=2))
  if part_1:
    return filter(lambda s: s in seats, [(i+di, j+dj) for di,dj in dirs])
  else:
    return filter(lambda s: s,
                  [next(ifilter(lambda s: s in seats, 
                                takewhile(lambda (i, j): 0 <= i < w and 0 <= j < h, 
                                          izip(count(i + di, di), count(j + dj, dj)))),
                        None) for di, dj in dirs])

def should_flip_seat(seats, part_1, s_idx, size):
  num_occupied = sum(seats[s] for s in adjacent_seats(seats, part_1, s_idx, size))
  return ((seats[s_idx] and num_occupied >= (4 if part_1 else 5))
          or (not seats[s_idx] and num_occupied == 0))

with open('11_input.txt') as f:
  seating = {(i, j): False for j, row in enumerate(f)
                           for i, seat in enumerate(row.strip())
                           if seat == 'L'}
  size = (max(i for i,_ in seating) + 1, max(j for _,j in seating) + 1)

for puzzle_part in (1,2):
  prev_seats, seats = None, seating
  while prev_seats != seats:
    prev_seats = seats
    seats = {idx: not s if should_flip_seat(prev_seats, puzzle_part==1, idx, size) 
                        else s
             for idx, s in seats.items()}
  print 'part %d: %d' % (puzzle_part, sum(seats.values()))
