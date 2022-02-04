#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')

# [[east faceing], [south faceing]]
# (row, col)
cucumbers = [[], []]
maxRow = maxCol = 0
with open(input, 'r') as f:
  row = -1
  lines = f.readlines()
  maxRow = len(lines)
  maxCol = len(lines[0].strip())
  for line in lines:
    row += 1
    col = -1
    for char in line.strip():
      col += 1
      if char == ">":
        cucumbers[0].append((row, col))
      elif char == "v":
        cucumbers[1].append((row, col))
  pass

movement = True
directions = [(0, 1), (1, 0)]
steps = 0
while movement:
  movement = False
  for herdCount in range(len(cucumbers)):
    rowAdd, colAdd = directions[herdCount]
    herd = cucumbers[herdCount]
    newHerd = []
    for cuCount in range(len(herd)):
      row, col = herd[cuCount]
      newRow = (row + rowAdd) % maxRow
      newCol = (col + colAdd) % maxCol
      if (newRow, newCol) not in cucumbers[0] + cucumbers[1]:
        newHerd.append((newRow, newCol))
        movement = True
      else:
        newHerd.append((row, col))
    cucumbers[herdCount] = newHerd
  steps += 1

print("Number of Steps: ", steps)