#!/usr/bin/python3
import os
import queue

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

nodes = []
with open(input, 'r') as f:
  for line in f.readlines():
    x, y = line.strip().split("-")
    nodes.append((x, y))

def part1():
  paths = queue.SimpleQueue()
  for nodeX, nodeY in nodes:
    if nodeX == "start":
      paths.put(["start", nodeY])
    elif nodeY == "start":
      paths.put(["start", nodeX])

  donePaths = []
  while not paths.empty():
    path = paths.get()
    lastNode = path[-1]
    if lastNode == "end": 
      donePaths.append(path)
      continue
    for nodeX, nodeY in nodes:
      if nodeX == lastNode and (nodeY.isupper() or nodeY not in path):
        paths.put(path + [nodeY])
      elif nodeY == lastNode and (nodeX.isupper() or nodeX not in path):
        paths.put(path + [nodeX])
  return(len(donePaths))

def part2():
  paths = queue.SimpleQueue()
  for nodeX, nodeY in nodes:
    if nodeX == "start":
      paths.put(["start", nodeY])
    elif nodeY == "start":
      paths.put(["start", nodeX])

  donePaths = []
  while not paths.empty():
    path = paths.get()
    lastNode = path[-1]
    hasDoubleVisit = len([val for val in path if val.islower() and path.count(val) > 1]) > 0
    if lastNode == "end": 
      donePaths.append(path)
      continue
    for nodeX, nodeY in nodes:
      nextNode = None
      if nodeX == lastNode:
        nextNode = nodeY
      elif nodeY == lastNode:
        nextNode = nodeX

      if nextNode != None and nextNode != "start":
        if nextNode.isupper():
          paths.put(path + [nextNode])
        elif nextNode not in path or not hasDoubleVisit:
          paths.put(path + [nextNode])
  return(len(donePaths))

print("Part 1: ", part1())
print("Part 2: ", part2())