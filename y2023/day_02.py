from collections import defaultdict
from operator import mul
from functools import reduce

data_files = [
  'day_02_input.txt',
  'day_02_test_input.txt'
]

def parse_data(filename):
  # Get the max draws for each colour
  # "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
  # becomes: {'red': 4, 'green': 2, 'blue': 6}
  data = open(filename).readlines()
  g = [[(d.split()[1], int(d.split()[0]))
        for d in g.strip().split(': ')[1].replace(';',',').split(', ')]
       for g in data]
  games = []
  for game in g:
    maxes = {'red': 0, 'green': 0, 'blue': 0} 
    for draw in game:
      maxes[draw[0]] = max(maxes[draw[0]], draw[1])
    games.append(maxes)
  return games

def part1(games):
  bag = {'red': 12, 'green': 13, 'blue': 14}
  return sum(i+1
             for i,g in enumerate(games)
             if all(g[m] <= bag[m] for m in bag))

def part2(games):
  return sum(reduce(mul, g.values()) for g in games)

if __name__ == '__main__':
  data = [parse_data(f) for f in data_files]
  p1_test = part1(data[1])
  p2_test = part2(data[-1])
  p1 = part1(data[0])
  p2 = part2(data[0])
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 8 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 2286 else '(failed)')
  print('Part 1:', p1)
  print('Part 2:', p2)
