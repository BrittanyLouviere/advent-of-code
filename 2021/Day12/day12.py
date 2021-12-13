#!/usr/bin/python3
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

memo = {}
def recurse(lastNode : str, visitedSmall : str, hasDouble : bool):
  answer = memo.get((lastNode, visitedSmall, hasDouble), None)
  if answer is not None: return answer # if answer already found, return it

  visited = [val for val in visitedSmall.split("-") if val != '']
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
    elif newNode not in visited:
      part1Count, part2Count = recurse(newNode, "-".join(sorted(visited + [newNode])), hasDouble)
    elif not hasDouble:
      part1Count, part2Count = recurse(newNode, visitedSmall, True)
    part1Total += part1Count
    part2Total += part2Count

  memo[(lastNode, visitedSmall, hasDouble)] = (part1Total, part2Total)
  return (part1Total, part2Total)

part1, part2 = recurse("start", "", False)
print("Part 1: ", part1)
print("Part 2: ", part2)