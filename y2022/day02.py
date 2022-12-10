turns = [(ord(t[0]) - ord('A'), 
          ord(t[2]) - ord('X'))
         for t in open('day02_input.txt').readlines()]

print('part 1:', sum(t[1] + 1 + 3 * ((t[1] - t[0] + 1) % 3) for t in turns))
print('part 2:', sum(3 * t[1] + ((t[0] + t[1] - 1) % 3) + 1 for t in turns))

