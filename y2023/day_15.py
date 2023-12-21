from collections import defaultdict
from functools import reduce

data_files = [
  'day_15_input.txt',
  'day_15_test_input.txt'
]

def parse_data(filename):
  return open(filename).read().strip().split(',')

def puzzle_hash(text):
  return reduce(lambda result, c: (17 * (result + ord(c))) % 256, text, 0)

def part1(data):
  return sum(puzzle_hash(text) for text in data)

def part2(data):
  # Only works for Python 3.7 or greater where dicts preserve insertion order.
  # On earlier Pythons this would need to be rewritten so that boxes is a dict
  # of hash -> list of labels, with a separate dict of label -> focal_length.
  boxes = defaultdict(dict)
  for command in data:
    label, focal_len = ((command[:-1], None) if command[-1] == '-'
                        else (command[:-2], int(command[-1])))
    box_num = puzzle_hash(label)
    if not focal_len:
      if label in boxes[box_num]:
        del boxes[box_num][label]
    else:
      boxes[box_num][label] = focal_len
  return sum((box_num+1) * (slot+1) * focal_len
             for box_num, labels in boxes.items()
             for slot, focal_len in enumerate(labels.values()))

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 1320 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 145 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
