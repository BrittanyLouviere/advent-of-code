#!/usr/bin/python3
import os
#import queue

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

nodes = {}
# key: node, value: array all connected nodes
# skips putting "start"
# skips adding an "end" key
with open(input, 'r') as f:
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

part1DonePaths = 0
part2DonePaths = 0

# set up starting paths
# (path array, has repeated small boolean)
paths = []
for node in nodes["start"]:
  if node == "end": 
    part1DonePaths += 0
    part2DonePaths += 1
  else: paths.append(([node], False))

# depth first search
while len(paths) > 0:
  path, hasDouble = paths.pop()
  lastNode = path[-1]
  for newNode in nodes[lastNode]:
    if newNode == "end":
      part2DonePaths += 1
      if not hasDouble: part1DonePaths += 1
    elif newNode.isupper() or newNode not in path or not hasDouble:
      paths.append((path + [newNode], hasDouble or (newNode.islower() and newNode in path)))

print("Part 1: ", part1DonePaths)
print("Part 2: ", part2DonePaths)