
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
 
def first_digit(line, reverse=False, words=False):
  line_len = len(line)
  for i in range(len(line)-2, -1, -1) if reverse else range(len(line)):
    if line[i].isdigit():
      return int(line[i])
    if words and i+3 < line_len:
      i2 = i
      t = word_trie.get(line[i2])
      while t:
        if type(t) == int:
          return t
        i2 += 1
        if i2 >= line_len:
          break
        t = t.get(line[i2])
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
