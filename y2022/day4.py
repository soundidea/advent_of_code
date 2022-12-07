import re
parser = re.compile(r'^(\d+)-(\d+),(\d+)-(\d+)')
pairs = map(parser.match, open('day4_input.txt'))
pairs = [tuple(map(int, p.groups())) for p in pairs]
pairs = [(set(range(p[0], p[1]+1)), set(range(p[2], p[3]+1))) for p in pairs]
print('part 1:', len(list(filter(lambda p: p[0] >= p[1] or p[1] >= p[0], pairs))))
print('part 2:', len(list(filter(lambda p: len(p[0] & p[1]), pairs))))
