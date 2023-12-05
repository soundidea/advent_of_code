from collections import defaultdict
from operator import mul
from functools import reduce


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

games = parse_data('day_02_input.txt')
test_games = parse_data('day_02_test_input.txt')

def part1(test=False):
  bag = {'red': 12, 'green': 13, 'blue': 14}
  return sum(i+1
             for i,g in enumerate(test_games if test else games)
             if all(g[m] <= bag[m] for m in bag))

def part2(test=False):
  return sum(reduce(mul, g.values()) for g in (test_games if test else games))

if __name__ == '__main__':
  p1_test = part1(test=True)
  p2_test = part2(test=True)
  print('Part 1 test:', p1_test, '(passed)' if p1_test == 8 else '(failed)')
  print('Part 2 test:', p2_test, '(passed)' if p2_test == 2286 else '(failed)')
  print('Part 1:', part1())
  print('Part 2:', part2())

