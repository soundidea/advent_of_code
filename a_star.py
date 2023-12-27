from collections import defaultdict
from dataclasses import dataclass, field
from queue import PriorityQueue
from typing import Any
import math

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

def reconstruct_path(came_from, current):
  path = [current]
  while current in came_from:
    current = came_from[current]
    path.append(current)
  return path[::-1]

def a_star(start, is_finished, heuristic, neighbours, edge_weight):
  '''Perform an A-star search and return the resulting path.

  Args:
      start: The starting position.
      is_finished: function(pos) -> bool, is the search done at 'pos'?
      heuristic: function(pos) -> number, best guess at how far until done.
      neighbours: function(pos, came_from) -> list, all the legal possible next steps.
      edge_weight: function(pos, next_pos) -> number, the cost of the edge.

  Returns:
      The resulting path.
  '''
  g_score = defaultdict(lambda: math.inf)
  g_score[start] = 0
  f_score = heuristic(start)
  open_set = PriorityQueue()
  open_set.put(PrioritizedItem(f_score, start))
  came_from = dict()
  while not open_set.empty():
    current = open_set.get().item
    if is_finished(current):
      return reconstruct_path(came_from, current)
    for neighbour in neighbours(current):
      new_g_score = g_score[current] + edge_weight(current, neighbour)
      if new_g_score < g_score[neighbour]:
        came_from[neighbour] = current
        g_score[neighbour] = new_g_score
        f_score = new_g_score + heuristic(neighbour)
        # If neighbour is already in open_set then delete it before re-adding
        # with the new f_score. This only works because PriorityQueue is a list
        # under the hood.
        open_set.queue = list(filter(lambda x: x.item != neighbour,
                                     open_set.queue))
        open_set.put(PrioritizedItem(f_score, neighbour))
  # Failure, no path was found.
  return []
