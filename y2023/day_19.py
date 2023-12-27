data_files = [
  'day_19_input.txt',
  'day_19_test_input.txt'
]

def parse_data(filename):
  workflows, parts = (x.split('\n')
                      for x in open(filename).read().strip().split('\n\n'))
  workflows = dict(w[:-1].split('{') for w in workflows)
  workflows = {n : v.split(',') for n,v in workflows.items()}
  parts = [tuple(int(v[2:]) for v in p[1:-1].split(',')) for p in parts]
  return workflows, parts

def split_one_range(lo, hi, op, n):
  if op == '<':
    if hi < n:
      return (lo,hi), None
    elif lo >= n:
      return None, (lo,hi)
    else:
      hi_in, lo_out = min(hi, n-1), max(lo, n)
      return (lo, hi_in), (lo_out, hi)
  else:  # op == '>'
    if lo > n:
      return (lo,hi), None
    elif hi <= n:
      return None, (lo,hi)
    else:
      lo_in, hi_out = max(lo, n+1), min(hi, n)
      return (lo_in, hi), (lo, hi_out)

def split_range(rng, rule):
  xl,xh,ml,mh,al,ah,sl,sh = rng
  var, op, n = rule[0], rule[1], int(rule[2:])
  lo_idx = 2 * 'xmas'.index(var)
  hi_idx = lo_idx + 1
  in_, out_ = split_one_range(rng[lo_idx], rng[hi_idx], op, n)
  if not in_:
    return None, rng
  elif not out_:
    return rng, None
  else:
    if var == 'x':
      return (in_ + rng[2:], out_ + rng[2:])
    elif var == 'm':
      return (rng[:2] + in_ + rng[4:], rng[:2] + out_ + rng[4:])
    elif var == 'a':
      return (rng[:4] + in_ + rng[6:], rng[:4] + out_ + rng[6:])
    elif var == 's':
      return (rng[:6] + in_, rng[:6] + out_)

def process(ranges, workflows):
  accepted = 0
  while len(ranges):
    workflow, in_ = ranges.pop()
    for rule in workflows[workflow]:
      r = rule.split(':')
      dest = r[-1]
      out = None
      if len(r) > 1:
        in_, out_ = split_range(in_, r[0])
        if not in_:
          in_ = out_
          continue
      xl,xh,ml,mh,al,ah,sl,sh = in_
      n_combos = (xh-xl+1) * (mh-ml+1) * (ah-al+1) * (sh-sl+1)
      if dest == 'A':
        accepted += n_combos
      elif dest != 'R' and n_combos:
        ranges.append((dest, in_))
      if not out_:
        break
      in_ = out_
  return accepted
  
def part2(data):
  workflows = data[0]
  ranges = [('in', (1, 4000, 1, 4000, 1, 4000, 1, 4000))]
  return process(ranges, workflows)

def part1(data):
  workflows, parts = data
  total = 0
  for x,m,a,s in parts:
    ranges = [('in', (x,x,m,m,a,a,s,s))]
    if process(ranges, workflows):
      total += sum((x,m,a,s))
  return total

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 19114 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 167409079868000 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
