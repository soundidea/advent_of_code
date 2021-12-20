from functools import reduce

def commonest(report, idx):
  '''Find the commonest line[idx] for line in report. Return '1' if it's a tie.'''
  return '1' if sum(int(line[idx]) for line in report) >= int((len(report)+1)/2) else '0'

report = [line.strip() for line in open('03_input.txt').readlines()]
num_digits = len(report[0])
gamma = int(''.join([commonest(report, idx) for idx in range(num_digits)]), 2)
epsilon = gamma ^ (2 ** num_digits - 1)
print('part 1:', gamma * epsilon)

o2 = reduce(lambda r, idx: r if len(r) == 1
                             else list(filter(lambda rl: rl[idx] == commonest(r, idx), r)),
            range(num_digits),
            report)
co2 = reduce(lambda r, idx: r if len(r) == 1
                              else list(filter(lambda rl: rl[idx] != commonest(r, idx), r)),
             range(num_digits),
             report)
print('part 2:', int(o2[0],2) * int(co2[0],2))
