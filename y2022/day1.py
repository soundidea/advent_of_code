elves = [sum(int(snack) for snack in elf.split('\n'))
         for elf in open('day1_input.txt').read().strip().split('\n\n')]
print('part 1:', max(elves))
print('part 2:', sum(sorted(elves)[-3:]))
