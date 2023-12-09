data_files = [
  'day_01_input.txt',
  'day_01_test_input.txt',
  'day_01_test_input_2.txt'
]

def parse_data(filename):
  return open(filename).readlines()

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
  for c in (line[::-1] if reverse else line):
    if c.isdigit():
      return int(c)
    if words:
      t = t.get(c, trie)
      if type(t) == int:
        return t
  raise ValueError('no digits found in %s' % line)

def part1(doc):
  return sum(10 * first_digit(l) +
             first_digit(l, reverse=True)
             for l in doc)

def part2(doc):
  return sum(10 * first_digit(l, words=True) +
             first_digit(l, reverse=True, words=True)
             for l in doc)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 142 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 281 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
