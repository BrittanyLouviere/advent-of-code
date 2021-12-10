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
      if x == "(" or x == "[" or x == "{" or x == "<":
        openChunks.append(x)
      else:
        lastChunk = openChunks[-1]
        if ((lastChunk == "(" and x == ")")
        or (lastChunk == "[" and x == "]")
        or (lastChunk == "{" and x == "}")
        or (lastChunk == "<" and x == ">")):
          openChunks.pop(-1)
        else: #corrupted
          corrupted = True
          if x == ")":
            corruptionPoints += 3
          elif x == "]":
            corruptionPoints += 57
          elif x == "}":
            corruptionPoints += 1197
          elif x == ">":
            corruptionPoints += 25137
    if corrupted == True: continue #don't calculate completion points if corrupted
    for x in reversed(openChunks):
      completionPoints *= 5
      if x == "(":
        completionPoints += 1
      elif x == "[":
        completionPoints += 2
      elif x == "{":
        completionPoints += 3
      elif x == "<":
        completionPoints += 4
    completionPointsList.append(completionPoints)


print("Part 1: ", corruptionPoints)
completionPointsList.sort()
x = int(len(completionPointsList) / 2)
print("Part 2: ", completionPointsList[x])