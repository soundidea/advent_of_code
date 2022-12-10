def sign(x):
  return (x > 0) - (x < 0)

def simulate(moves, n):
  knots = [0j for _ in range(n)]
  visited = set([0j])
  for m in moves:
    for _ in range(int(m[2:])):
      knots[0] += {'L': -1, 'R': 1, 'U': 1j, 'D': -1j}[m[0]]
      for k in range(1,n):
        d = knots[k-1] - knots[k]
        if abs(d) > 1.42:
          knots[k] += complex(sign(d.real), sign(d.imag))
      visited.add(knots[-1])
  return len(visited)

moves = open('day09_input.txt').read().strip().split('\n')
print('part 1:', simulate(moves, 2))
print('part 2:', simulate(moves, 10))

