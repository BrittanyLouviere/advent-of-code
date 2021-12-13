#!/usr/bin/python3
from functools import lru_cache
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

nodes = {}
# key: node, value: array all connected nodes
# skips adding "start" in values
# skips adding an "end" key
with open(bigboy, 'r') as f:
  for line in f.readlines():
    x, y = line.strip().split("-")
    if y != "start":
      if x in nodes:
        nodes[x].append(y)
      elif x != "end":
        nodes[x] = [y]
    if x != "start":
      if y in nodes:
        nodes[y].append(x)
      elif y != "end":
        nodes[y] = [x]

@lru_cache(maxsize=4000000)
def recurse(lastNode : str, visitedSmall : frozenset, hasDouble : bool):
  part1Total = 0
  part2Total = 0
  for newNode in nodes[lastNode]:
    part1Count = 0
    part2Count = 0
    if newNode == "end":
      part2Count += 1
      if not hasDouble: part1Count += 1
    elif newNode.isupper():
      part1Count, part2Count = recurse(newNode, visitedSmall, hasDouble)
    elif newNode not in visitedSmall:
      part1Count, part2Count = recurse(newNode, visitedSmall.union({newNode}), hasDouble)
    elif not hasDouble:
      part1Count, part2Count = recurse(newNode, visitedSmall, True)
    part1Total += part1Count
    part2Total += part2Count

  return (part1Total, part2Total)

part1, part2 = recurse("start", frozenset(), False)
print("Part 1: ", part1)
print("Part 2: ", part2)