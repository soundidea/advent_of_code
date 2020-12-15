inputs = (16,11,15,0,1,7)
for part, count_to in enumerate((2020, 30000000)):
  last_indices = {n:i for i,n in enumerate(inputs[:-1])}
  prev = inputs[-1]
  for i in range(len(inputs) - 1, count_to - 1):
    if prev in last_indices:
      last_indices[prev], prev = i, i - last_indices[prev]
    else:
      last_indices[prev], prev = i, 0
  print 'part %d: %d' % (part + 1, prev)

