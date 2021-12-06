#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')
biggerboy = os.path.join(root, 'BiggerBoy.txt')


lines = []
with open(input, 'r') as f:
  for line in f:
    start, end = line.strip().split(" -> ")
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]
    if(start[0] < end[0]): lines.append(start + end)
    else: lines.append(end + start)
lines.sort()



hitCount = 0
hits = []
col = 0

while max(lines)[0] > -1:
  for line in lines:
    if (line[0] > col): break #break if column done
    while line[0] == col: #loop if line is verticle
      while (line[1] + 1 > len(hits)): hits.append(0) #lengthen hit array if needed
      hits[line[1]] += 1
      
      if(line[0] == line[2] and line[1] == line[3]): line[0] = -1 #mark this line as done
      else: #update line
        if(line[0] > line[2]): line[0] -= 1
        if(line[0] < line[2]): line[0] += 1
        if(line[1] > line[3]): line[1] -= 1
        if(line[1] < line[3]): line[1] += 1
  
  for x in hits: #count up hits
    if x > 1: hitCount += 1
  hits = [] #reset hit array
  col += 1 #increment column
  print("column: ", col)
print(hitCount)