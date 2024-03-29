from functools import reduce
# Yeah I could do this with a for loop but where's the fun in that?
_, history = reduce(lambda xh, i:
                        (xh[0] + int(i[5:]), xh[1] + [xh[0], xh[0]])
                        if i[0] == 'a'
                        else (xh[0], xh[1] + [xh[0]]),
                    open('day10_input.txt').read().strip().split('\n'),
                    (1, []))
print('part 1:', sum(i * history[i] for i in range(20,221,40)))
print('part 2:')
print('\n'.join(''.join('#' if abs(history[x0 + x] - x) <= 1
                            else ' '
                        for x in range(40))
                for x0 in range(0, len(history), 40)))
