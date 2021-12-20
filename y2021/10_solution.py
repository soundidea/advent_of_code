from functools import reduce

close = {'(': ')',
         '[': ']',
         '{': '}',
         '<': '>'}

corrupt_score = {')': 3,
                 ']': 57,
                 '}': 1197,
                 '>': 25137}

close_score = {')': 1,
               ']': 2,
               '}': 3,
               '>': 4}

def illegal(line):
  '''Either return the score of the first illegal char, or the
     closing scores for the unfinished stack in reverse order.'''
  stack = []
  for c in line:
    if c in close.keys():
      stack.append(close[c])
    elif c != stack.pop():
      return corrupt_score[c]
  return [close_score[s] for s in stack[::-1]]

lines = list(map(str.strip, open('10_input.txt').readlines()))
print('part 1:', sum(filter(lambda c: type(c) == int, map(illegal, lines))))
scores = sorted(reduce(lambda acc, c: c + acc * 5, stack, 0) for stack in 
                       filter(lambda c: type(c) == list, map(illegal, lines)))
print('part 2:', scores[int(len(scores) / 2)])
