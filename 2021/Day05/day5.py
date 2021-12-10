#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

grid = []
lines = []
with open(input, 'r') as f:
  for line in f:
    start, end = line.strip().split(" -> ")
    start = start.split(",")
    end = end.split(",")
    lines.append([int(x) for x in start + end])

size = max(map(max, lines)) + 1
grid = [[0] * size] * size
grid = [[0 for i in range(size)] for j in range(size)]

for line in lines:
  x = [line[0], line[1]]
  end = [line[2], line[3]]
  #if(x[0] != end[0] and x[1] != end[1]): continue #skip diagonals
  
  grid[x[1]][x[0]] += 1
  while (x[0] != end[0] or x[1] != end[1]):
    if(x[0] > end[0]): x[0] -= 1
    if(x[0] < end[0]): x[0] += 1
    if(x[1] > end[1]): x[1] -= 1
    if(x[1] < end[1]): x[1] += 1
    grid[x[1]][x[0]] += 1


#for line in grid:
#  print(line)

count = 0
for x in sum(grid, []):
  if x > 1: count += 1
print(count)