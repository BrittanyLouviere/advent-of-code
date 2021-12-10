#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

grid = {}
with open(input, 'r') as f:
  for line in f:
    start, end = line.strip().split(" -> ")
    x = [int(i) for i in start.split(",")]
    end = [int(i) for i in end.split(",")]

    #if(x[0] != end[0] and x[1] != end[1]): continue #skip diagonals
    key = (x[1], x[0])
    if (key not in grid): grid[key] = 0
    grid[key] += 1
    while (x[0] != end[0] or x[1] != end[1]):
      if(x[0] > end[0]): x[0] -= 1
      if(x[0] < end[0]): x[0] += 1
      if(x[1] > end[1]): x[1] -= 1
      if(x[1] < end[1]): x[1] += 1
      key = (x[1], x[0])
      if (key not in grid): grid[key] = 0
      grid[key] += 1

count = 0
for x in grid.values():
  if x > 1: count += 1
print(count)