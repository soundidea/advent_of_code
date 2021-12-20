
instruments = [[[''.join(sorted(r)) for r in section.split()]
                for section in line.strip().split(' | ')]
                for line in open('08_input.txt').readlines()]

print('part 1:', sum(len(digit) in [2,3,4,7]
                     for readings in instruments for digit in readings[1]))

def mappings(readings):
  '''Given 10 readings representing 10 digits, return them mapped to their digits.'''
  by_length = {l : list(filter(lambda r: len(r) == l, readings))
               for l in range(2,8)}
  one = by_length[2][0]
  # 3 = the len(5) digit with 1 as a subset
  # 6 = the len(6) digit without 1 as a subset
  # 9 = the len(6) digit with 3 as a subset
  # 0 = the remaining len(6) digit
  # 5 = the len(5) digit that makes 9 when combined with 1
  # 2 = the remaining len(5) digit
  three = next(filter(lambda r: set(one) < set(r), by_length[5]))
  six = next(filter(lambda r: not (set(one) < set(r)), by_length[6]))
  nine = next(filter(lambda r: set(three) < set(r), by_length[6]))
  zero = next(filter(lambda r: r not in [six, nine], by_length[6]))
  five = next(filter(lambda r: (set(one) | set(r)) == set(nine), by_length[5]))
  two = next(filter(lambda r: r not in [three, five], by_length[5]))
  return {zero: '0',
          one: '1',
          two: '2',
          three: '3',
          by_length[4][0]: '4',
          five: '5',
          six: '6',
          by_length[3][0]: '7',
          by_length[7][0]: '8',
          nine: '9'}

print('part 2:', sum(int(''.join(mappings(i[0])[digit] for digit in i[1])) for i in instruments))
