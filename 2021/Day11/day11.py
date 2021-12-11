#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

octopi = []
size = -1
with open(input, 'r') as f:
  row = 0
  for line in f.readlines():
    col = 0
    if size == -1: size = len(line.strip())
    octopi.append([0] * size)
    for num in line.strip():
      octopi[row][col] = int(num)
      col += 1
    row += 1

flashCount = 0
firstAllFlash = -1
days = 100
day = 0
while day < days or firstAllFlash == -1:
  day += 1
  flashQueue = []
  for row in range(size):
    for col in range(size):
      octopi[row][col] += 1
      if octopi[row][col] > 9:
        flashQueue.append((row, col))
  for row, col in flashQueue:
    for row2 in [row-1, row, row+1]:
      for col2 in [col-1, col, col+1]:
        if row2 > -1 and row2 < size and col2 > -1 and col2 < size:
          octopi[row2][col2] += 1
          if octopi[row2][col2] > 9 and (row2, col2) not in flashQueue: 
            flashQueue.append((row2, col2))
  for row, col in flashQueue:
    octopi[row][col] = 0
  flashes = len(flashQueue)
  if day <= days:
    flashCount += flashes
  if flashes == size**2 and firstAllFlash == -1:
    firstAllFlash = day

print("Part 1: ", flashCount)
print("Part 2: ", firstAllFlash)