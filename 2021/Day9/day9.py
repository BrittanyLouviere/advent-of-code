#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

grid = []
with open(input, 'r') as f:
  for line in f.readlines():
    grid.append([int(num) for num in line.strip()])

lows = {}
maxRow = len(grid)
maxCol = len(grid[0])
for row in range(maxRow):
  for col in range(maxCol):
    current = grid[row][col]
    if ((row == 0 or grid[row-1][col] > current)          #check above
    and (col == 0 or grid[row][col-1] > current)          #check left
    and (row == maxRow-1 or grid[row+1][col] > current)   #check below
    and (col == maxCol-1 or grid[row][col+1] > current)): #check right
      lows[(row, col)] = current

riskLevel = 0
for low in lows.values():
  riskLevel += low + 1
print("Part 1: ", riskLevel)

basins = []
for low in lows:
  basin = []
  basin.append((low[0], low[1]))
  for item in basin:
    row, col = item
    if col != 0 and grid[row][col-1] != 9 and (row, col-1) not in basin: #check left
      basin.append((row, col-1))
    if row != 0 and grid[row-1][col] != 9 and (row-1, col) not in basin:         #check above
      basin.append((row-1, col))
    if col != maxCol-1 and grid[row][col+1] != 9 and (row, col+1) not in basin:  #check right
      basin.append((row, col+1))
    if row != maxRow-1 and grid[row+1][col] != 9 and (row+1, col) not in basin:  #check below
      basin.append((row+1, col))
  basins.append(len(basin))

basins.sort(reverse=True)
x = 1
for i in range(3):
  x *= basins[i]
print("Part 2: ", x)