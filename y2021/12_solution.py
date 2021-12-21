from collections import Counter
import re

connections = [re.match(r'(\w+)-(\w+)\n', line).groups() for line in open('12_input.txt').readlines()]
graph = {room: [r for c in connections
                  for r in c
                  if room in c and r not in [room, 'start']]
         for room in set(r for c in connections for r in c)}
graph['end'] = []

def num_small_repeats(path):
  return sum(v - 1 for v in Counter(filter(str.islower, path)).values())

def complete_paths(graph, max_small_repeats):
  active_paths, completed_paths = [['start']], []
  while len(active_paths):
    new_paths = []
    for path in active_paths:
      next_rooms = [room for room in graph[path[-1]]
                         if room.isupper() or
                            room not in path or
                            num_small_repeats(path) < max_small_repeats]
      if len(next_rooms):
        new_paths.extend(path + [room] for room in next_rooms)
      elif path[-1] == 'end':
        completed_paths.append(path)
    active_paths = new_paths
  return completed_paths

print('part 1:', len(complete_paths(graph, 0)))
print('part 2:', len(complete_paths(graph, 1)))
