#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

corruptionPoints = 0
completionPointsList = []
with open(input, 'r') as f:
  for line in f.readlines():
    openChunks = []
    corrupted = False
    completionPoints = 0
    for x in line.strip():
      if corrupted == True: break #break out of loop if corruption found
      if x in "([{<":
        openChunks.append(x)
      else:
        lastChunk = openChunks[-1]
        if lastChunk + x in "()[]{}<>":
          openChunks.pop()
        else: #corrupted
          corrupted = True
          points = [3, 57, 1197, 25137]
          corruptionPoints += points[")]}>".index(x)]
    if corrupted == True: continue #don't calculate completion points if corrupted
    for x in reversed(openChunks):
      completionPoints *= 5
      completionPoints += "([{<".index(x) + 1
    completionPointsList.append(completionPoints)

print("Part 1: ", corruptionPoints)
completionPointsList.sort()
x = int(len(completionPointsList) / 2)
print("Part 2: ", completionPointsList[x])