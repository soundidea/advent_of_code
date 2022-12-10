import string

def priority(badge_set):
  badge = next(iter(badge_set))
  return (ord(badge) - ord('A') + 27
          if badge in string.ascii_uppercase
          else ord(badge) - ord('a') + 1)

packs = list(map(str.strip, open("day03_input.txt").readlines()))
print('part 1:', sum(map(priority,
                         [set(p[:len(p)//2]) & set(p[len(p)//2:])
                          for p in packs])))
print('part 2:', sum(map(priority,
                         [set(packs[i]) & set(packs[i+1]) & set(packs[i+2])
                          for i in range(0, len(packs), 3)])))
