#!/usr/bin/python3
import os
import numpy as np

array = np.array([[-1, -1], [-1, 0], [1, -1], [2, 3], [10, 4], [5, 10], [10, 10]])
x, y = ((array > -1) & (array < 10)).transpose()
test2 = array[x&y]

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

octopi = None
size = -1
with open(input, 'r') as f:
  row = 0
  for line in f.readlines():
    col = 0
    if size == -1: 
      size = len(line.strip())
      octopi = np.empty((size, size), dtype=int)
    for num in line.strip():
      octopi[row][col] = int(num)
      col += 1
    row += 1

flashCount = 0
firstAllFlash = -1
steps = 100
step = 0
while step < steps or firstAllFlash == -1:
  step += 1
  octopi += 1
  flashQueue : list = np.transpose(np.where(octopi > 9)).tolist()
  for row, col in flashQueue:
    neighbors = np.array(np.meshgrid([row-1, row, row+1], [col-1, col, col+1])).T.reshape(-1,2)
    x, y = ((neighbors > -1) & (neighbors < size)).transpose()
    neighbors = neighbors[x & y]
    for nRow, nCol in neighbors:
      octopi[nRow][nCol] += 1
      if octopi[nRow][nCol] > 9 and [nRow, nCol] not in flashQueue: 
        flashQueue.append([nRow, nCol])
  octopi[octopi > 9] = 0
  flashes = len(flashQueue)
  if step <= steps:
    flashCount += flashes
  if flashes == size**2 and firstAllFlash == -1:
    firstAllFlash = step

print("Part 1: ", flashCount)
print("Part 2: ", firstAllFlash)