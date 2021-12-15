#!/usr/bin/python3
import os
from math import ceil
from types import coroutine

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

grid = []
with open(input, 'r') as f:
  for line in f.readlines():
    grid.append(line.strip())

def part1():
  maxX = len(grid[0])
  maxY = len(grid)
  paths = {}
  paths[(0, 0)] = 0
  visited = set()
  while True:
    x, y = min(paths, key=paths.get)
    if x == maxX-1 and y == maxY-1: #we found it!
      return min(paths.values())
    for newX, newY in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
      if -1 < newX < maxX and -1 < newY < maxY and (newX, newY) not in visited:
        oldNum = paths.get((newX, newY))
        newNum = paths[(x, y)] + int(grid[newY][newX])
        if oldNum is None or oldNum > newNum:
          paths[(newX, newY)] = newNum
    del paths[(x, y)]
    visited.add((x, y))

def digitSum(n):
  r = 0
  while n:
      r, n = r + n % 10, n // 10
  return r

def part2():
  sizeX = len(grid[0])
  sizeY = len(grid)
  maxX = len(grid[0]) * 5
  maxY = len(grid) * 5
  paths = {}
  paths[(0, 0)] = 0
  visited = set()
  while True:
    x, y = min(paths, key=paths.get)
    if x == maxX-1 and y == maxY-1: #we found it!
      return min(paths.values())
    
    for newX, newY in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
      if -1 < newX < maxX and -1 < newY < maxY and (newX, newY) not in visited:
        oldNum = paths.get((newX, newY))
        additive = (newX // sizeX) + (newY // sizeY)
        value = digitSum((int(grid[newY % sizeX][newX % sizeY]) + additive))
        newNum = paths[(x, y)] + value
        if oldNum is None or oldNum > newNum:
          paths[(newX, newY)] = newNum
    del paths[(x, y)]
    visited.add((x, y))

print("Part 1: ", part1())
print("Part 2: ", part2())