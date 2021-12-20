def count_increases(values):
  '''Count the number of times values[n+1] > values[n].'''
  return sum(a < b for (a,b) in zip(values[:-1], values[1:]))

soundings = [int(depth) for depth in open('01_input.txt').readlines()]
print('part 1:', count_increases(soundings))

threesums = [sum(soundings[a:a+3]) for a in range(len(soundings)-2)]
print('part 2:', count_increases(threesums))
 
