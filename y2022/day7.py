from collections import defaultdict
log = map(str.strip, open('day7_input.txt').readlines()[1:])
dirs = defaultdict(int)
path = []
for l in log:
  if l == '$ cd ..':
    path.pop()
  elif l[:4] == '$ cd':
    path.append(l[5:])
  elif l[0].isnumeric():
    sz = int(l.split(' ')[0])
    for d in range(len(path)+1):
      dirs['/'.join(path[:d])] += sz

print('part 1:', sum(d[1] for d in filter(lambda d: d[1] <= 100000, dirs.items())))
print('part 2:', min(d[1] for d in filter(lambda d: d[1] >= dirs[''] - 40000000, dirs.items())))
