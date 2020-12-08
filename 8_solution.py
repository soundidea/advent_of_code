# Only needed in Python 2, in Python 3 just use builtin filter()
from itertools import ifilter


opcode = {
  'acc': lambda arg, acc, pc: (acc + arg, pc + 1),
  'jmp': lambda arg, acc, pc: (acc, pc + arg),
  'nop': lambda arg, acc, pc: (acc, pc + 1)
}


def run_program(prog):
  acc, pc, visited_pcs = (0, 0, [])
  while pc not in visited_pcs and pc < len(prog):
    visited_pcs.append(pc)
    acc, pc = opcode[prog[pc][0]](prog[pc][1], acc, pc)
  return acc, pc


if __name__ == '__main__':
  with open('8_input.txt') as f:
    boot = [(op, int(arg)) for (op, arg) in [l.split(' ') for l in f.readlines()]]

  print 'part 1: %d' % run_program(boot)[0]

  flip = {'jmp': 'nop', 'nop': 'jmp'}
  all_outcomes = iter(run_program(boot[:i] + [(flip[op], arg)] + boot[i+1:]) for i, (op, arg) in enumerate(boot) if op in flip)
  print 'part 2: %d' % next(ifilter(lambda (_, pc): pc >= len(boot), all_outcomes))[0]
