#!/usr/bin/python3
import os
import heapq
from dataclasses import dataclass, field

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

grid = []
with open(input, 'r') as f:
  for line in f.readlines():
    grid.append(line.strip())

@dataclass(order=True)
class PathPoint:
  priority: int
  cost: int=field(compare=False)
  coord: tuple=field(compare=False)
  
  def __init__(self, cost, coord, maxX, maxY) -> None:
    self.cost = cost
    self.coord = coord
    self.priority = cost + (maxX - coord[0]) + (maxY - coord[1])

def digitSum(n):
  r = 0
  while n:
      r, n = r + n % 10, n // 10
  return r

sizeX = len(grid[0])
sizeY = len(grid)
def findPath(gridMult:int):
  maxX = sizeX * gridMult
  maxY = sizeY * gridMult
  paths = []
  visited = set()
  currentPoint = PathPoint(0, (0, 0), maxX, maxY)

  while currentPoint.coord != (maxX-1, maxY-1):
    x, y = currentPoint.coord
    currentCost = currentPoint.cost
    for newX, newY in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
      if -1 < newX < maxX and -1 < newY < maxY and (newX, newY) not in visited:
        additive = (newX // sizeX) + (newY // sizeY)
        value = digitSum((int(grid[newY % sizeX][newX % sizeY]) + additive))
        newCost = currentCost + value
        heapq.heappush(paths, PathPoint(newCost, (newX, newY), maxX, maxY))
    visited.add((x, y))
    while currentPoint.coord in visited:
      currentPoint = heapq.heappop(paths)

  return currentPoint.cost

print("Part 1: ", findPath(1))
print("Part 2: ", findPath(5))