from itertools import count

def transform(subject, loop_size):
  return reduce(lambda a,_: (a * subject) % 20201227, range(loop_size), 1)

public_keys = [int(l) for l in open('25_input.txt')]
#public_keys = [5764801, 17807724]

loop_sizes = []
for pub_k in public_keys:
  k = 1
  for l in count(1):
    k = (k * 7) % 20201227
    if k == pub_k:
      break
  loop_sizes.append(l)

print transform(public_keys[0], loop_sizes[1])
print transform(public_keys[1], loop_sizes[0])
