from collections import Counter
from functools import reduce

template, rules = map(str.strip, open('14_input.txt').read().split('\n\n'))
template = list(''.join(pair) for pair in zip(template[:-1], template[1:]))
rules = {r[:2] : (''.join([r[0], r[6]]), ''.join([r[6], r[1]]))
         for r in rules.split('\n')}

def apply_steps(template, num_steps):
  '''Given a template as a list of letter pairs (e.g. ['NN', 'NC', 'CB'] for NNCB)
     Apply rule substitution `num_steps` times, and return the letter frequencies
     of the resulting polymer.'''
  pair_counts = reduce(
      lambda pc,_: reduce(Counter.__add__,
                          [Counter({child: count for child in rules[pair]})
                              for pair, count in pc.items()]),
      range(num_steps),
      Counter(template))
  return reduce(lambda c, pc: c + Counter({pc[0][1]: pc[1]}),
                pair_counts.items(),
                Counter(template[0][0]))

counts = apply_steps(template, 10)
print('part 1:', max(counts.values()) - min(counts.values()))
counts = apply_steps(template, 40)
print('part 2:', max(counts.values()) - min(counts.values()))

