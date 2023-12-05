word_trie = {
  'o': {'n': {'e': 1}},
  't': {'w': {'o': 2},
        'h': {'r': {'e': {'e': 3}}}},
  'f': {'o': {'u': {'r': 4}},
        'i': {'v': {'e': 5}}},
  's': {'i': {'x': 6},
        'e': {'v': {'e': {'n': 7}}}},
  'e': {'i': {'g': {'h': {'t': 8}}}},
  'n': {'i': {'n': {'e': 9}}}
}
 
reverse_word_trie = {
  'e': {'n': {'o': 1,
              'i': {'n': 9}},
        'e': {'r': {'h': {'t': 3}}},
        'v': {'i': {'f': 5}}},
  'o': {'w': {'t': 2}},
  'r': {'u': {'o': {'f': 4}}},
  'x': {'i': {'s': 6}},
  'n': {'e': {'v': {'e': {'s': 7}}}},
  't': {'h': {'g': {'i': {'e': 8}}}}
}

def first_digit(line, reverse=False, words=False):
  if words:
    trie = reverse_word_trie if reverse else word_trie
    t = trie
  for c in (line[-2::-1] if reverse else line[:-1]):
    if c.isdigit():
      return int(c)
    if words:
      t = t.get(c, trie)
      if type(t) == int:
        return t
  raise ValueError('no digits found in %s' % line)

doc = open('day_01_input.txt').readlines()
part1_test_doc = open('day_01_test_input.txt').readlines()
part2_test_doc = open('day_01_test_input_2.txt').readlines()

def part1(test=False):
  data = part1_test_doc if test else doc
  return sum(10 * first_digit(l) +
             first_digit(l, reverse=True)
             for l in data)

def part2(test=False):
  data = part2_test_doc if test else doc
  return sum(10 * first_digit(l, words=True) +
             first_digit(l, reverse=True, words=True)
             for l in data)

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 142 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 281 else '(failed)')
  print('Part 1:', part1())
  print('Part 2:', part2())
