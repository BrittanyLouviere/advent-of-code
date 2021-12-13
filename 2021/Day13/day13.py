#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

dots = set()
instructions = []
with open(input, 'r') as f:
  for line in f.readlines():
    if "," in line:
      x, y = line.strip().split(",")
      dots.add((int(x), int(y)))
    elif "fold" in line:
      dir, num = line.replace("fold along ", "").strip().split("=")
      instructions.append((dir, int(num)))

def fold(direction, num):
  if direction == "y":
    s = [val for val in dots if val[1] > num]
    for x, y in s:
      dots.discard((x, y))
      y = abs(y - num - num)
      dots.add((x,y))
  else:
    s = [val for val in dots if val[0] > num]
    for x, y in s:
      dots.discard((x, y))
      x = abs(x - num - num)
      dots.add((x,y))

printed = False
for dir, num in instructions:
  fold(dir, num)
  if not printed:
    print("Part 1: ", len(dots))
    printed = True

grid = [[]]
while len(dots) > 0:
  col, row = dots.pop()
  while len(grid) <= row:
    grid.append([])
  while len(grid[row]) <= col:
    grid[row] += " "
  grid[row][col] = "\u2588"

for line in grid:
  print("".join(line))