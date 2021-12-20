from collections import Counter
import re

connections = [re.match(r'(\w+)-(\w+)\n', line).groups() for line in open('12_input.txt').readlines()]
#connections = [re.match(r'(\w+)-(\w+)\n', line).groups() for line in open('12_test_input_1.txt').readlines()]
graph = {node: [r for c in connections
                  for r in c
                  if node in c and r not in [node, 'start']]
         for node in set(r for c in connections for r in c)}
graph['end'] = []

def num_small_repeats(path):
  return sum(v - 1 for v in Counter(filter(str.islower, path)).values())

def complete_paths(graph, max_small_repeats):
  active_paths, completed_paths = [['start']], []
  while len(active_paths):
    new_paths = []
    for path in active_paths:
      next_rooms = [node for node in graph[path[-1]]
                         if node.isupper() or 
                            node not in path or
                            num_small_repeats(path) < max_small_repeats]
      if len(next_rooms):
        new_paths.extend(path + [node] for node in next_rooms)
      elif path[-1] == 'end':
        completed_paths.append(path)
    active_paths = new_paths
  return completed_paths

print('part 1:', len(complete_paths(graph, 0)))
print('part 2:', len(complete_paths(graph, 1)))
