import re
from collections import Counter
from itertools import chain
from operator import mul

#tiles = open('20_test_input.txt').read().split('\n\n')
tiles = open('20_input.txt').read().split('\n\n')
tiles = {int(re.match(r'Tile (\d+):', t.splitlines()[0]).group(1)): t.splitlines()[1:] for t in tiles}

edges = {i: [t[0], t[-1], ''.join(l[0] for l in t), ''.join(l[-1] for l in t)] for i,t in tiles.items()}
c = Counter(chain.from_iterable(edges.values()))

outside_edges = filter(lambda edge: c[edge] + c[edge[::-1]] == 1, chain.from_iterable(edges.values()))

corners = reduce(mul, (c[0] for c in filter(lambda (i,ne): ne==2, [(i, sum(1 for e in eds if e in outside_edges or e[::-1] in outside_edges)) for i,eds in edges.items()])))
print corners



# for each tile there are 8 possible orientations, 4 rotations, plus flip then 4 more rotations
def tile_orientations(tile):
  for o in (tile, tile[::-1]):
    ninety_cw = [''.join(o[i-1][j] for i in range(len(o), 0, -1)) for j in range(len(o[0]))]
    # no rotation
    yield o
    # 90 deg CW
    yield ninety_cw
    # 180 deg
    yield [row[::-1] for row in o[::-1]]
    # 90 deg CCW
    yield [row[::-1] for row in ninety_cw[::-1]]

for o in tile_orientations(tiles[3209]):
  print '\n'.join(o) + '\n'

#import collections
#import itertools
#import math
#import re
#import sys
#
#tiles = [l.rstrip('\n') for l in open('20_test_input.txt').read().split('\n\n')]
#
#def edges(lines):
#    lines = lines.split('\n')
#    return [''.join(l[0] for l in lines)[::-1], lines[0], ''.join(l[-1] for l in lines), lines[-1][::-1]]
#
#def flip(lines):
#    lines = lines.split('\n')
#    return '\n'.join(l[::-1] for l in lines)
#
#def rot(lines):
#    lines = lines.split('\n')
#    s = []
#    for row in range(len(lines)):
#        s.append(''.join(l[-1-row] for l in lines))
#    return '\n'.join(s)
#
#edgecount = collections.defaultdict(int)
#edgetotile = collections.defaultdict(list)
#tdict = {}
#for tile in tiles:
#    head, lines = tile.split('\n', 1)
#    tnum = int(head[5:-1])
#    tdict[tnum] = lines
#
#    ee = edges(lines)
#    for e in ee:
#        e = min(e, e[::-1])
#        edgecount[e] += 1
#        edgetotile[e].append(tnum)
#
#
#used = set()
#
#assembly = [[]]
#
#def go():
#    p = 1
#    for tile in tiles:
#        head, lines = tile.split('\n', 1)
#        tnum = int(head[5:-1])
#
#        uq = 0
#        for e in edges(lines):
#            e = min(e, e[::-1])
#            if edgecount[e] == 1:
#                uq += 1
#        if uq == 2:
#            # print(tnum)
#            p *= tnum
#
#            # for part 1, remove the following code:
#            ll = lines
#            for _ in range(4):
#                e = edges(ll)
#                if edgecount[min(e[0], e[0][::-1])] == 1 and edgecount[min(e[1], e[1][::-1])] == 1:
#                    assembly[0].append(ll)
#                    used.add(tnum)
#                    return
#                ll = flip(ll)
#                if edgecount[min(e[0], e[0][::-1])] == 1 and edgecount[min(e[1], e[1][::-1])] == 1:
#                    assembly[0].append(ll)
#                    used.add(tnum)
#                    return
#                ll = flip(ll)
#                ll = rot(ll)
#            assert False
#    # print(p)
#go()
#
#def k(edge):
#    return min(edge, edge[::-1])
#
## fill first row
#while True:
#    tile = assembly[0][-1]
#    edge = edges(tile)[2][::-1]
#    nextt = next((tnum for tnum in edgetotile[k(edge)] if tnum not in used), None)
#    if not nextt:
#        # end of row
#        break
#    ll = tdict[nextt]
#    for _ in range(4):
#        if edges(ll)[0] == edge:
#            break
#        ll = flip(ll)
#        if edges(ll)[0] == edge:
#            break
#        ll = flip(ll)
#        ll = rot(ll)
#    else:
#        assert False
#    assembly[0].append(ll)
#    used.add(nextt)
#
#def printrow(row):
#    for chunks in itertools.zip_longest(*(r.split('\n') for r in row), fillvalue=' '*8):
#        print(' '.join(chunks))
#    print()
#
#def join(assembly):
#    rows = collections.defaultdict(str)
#    for mr, row in enumerate(assembly):
#        for chunk in row:
#            chunklines = chunk.split('\n')
#            for r, subrow in enumerate(chunklines):
#                if r not in (0, len(chunklines) - 1):
#                    rows[100*mr + r] += subrow[1:-1]
#    return '\n'.join(v for k, v in sorted(rows.items()))
#
#
## fill rest of rows
#while len(used) < len(tdict):
#    newrow = []
#    for tile in assembly[-1]:
#        edge = edges(tile)[3][::-1]
#        nextt = next((tnum for tnum in edgetotile[k(edge)] if tnum not in used), None)
#        if not nextt:
#            # end of row
#            break
#        ll = tdict[nextt]
#        for _ in range(4):
#            if edges(ll)[1] == edge:
#                break
#            ll = flip(ll)
#            if edges(ll)[1] == edge:
#                break
#            ll = flip(ll)
#            ll = rot(ll)
#        else:
#            assert False
#        newrow.append(ll)
#        used.add(nextt)
#    assert len(newrow) == len(assembly[-1])
#    assembly.append(newrow)
#
#seamonster = '''\
#                  # \n\
##    ##    ##    ###
# #  #  #  #  #  #   '''.split('\n')
#
#joined = join(assembly)
#
#def look(joined):
#    fc = 0
#    for row in range(len(joined)):
#        for col in range(len(joined[0])):
#            found = True
#            for r in range(len(seamonster)):
#                # print('r is', r)
#                for c in range(len(seamonster[0])):
#                    # print('c is', c, repr(seamonster[r][c]))
#                    if seamonster[r][c] != '#':
#                        continue
#                    try:
#                        # print('sm', r, c, joined[row+r][col+c])
#                        if joined[row+r][col+c] != '#':
#                            found = False
#                    except IndexError:
#                        found = False
#                        pass
#            if found:
#                # print('found at', row, col)
#                fc += 1
#    return fc
#
#jj = joined
#for _ in range(4):
#    k = look(jj.split('\n'))
#    if k:
#        break
#    jj = flip(jj)
#    k = look(jj.split('\n'))
#    if k:
#        break
#    jj = flip(jj)
#    jj = rot(jj)
#
#
#print(jj)
#print(jj.count('#') - ''.join(seamonster).count('#') * k)
#
