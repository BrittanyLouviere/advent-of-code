#!/usr/bin/python3
import os
import math
import asyncio
from types import coroutine

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')
biggerboy = os.path.join(root, 'BiggerBoy.txt')

lines = []
with open(biggerboy, 'r') as f:
  for line in f:
    start, end = line.strip().split(" -> ")
    start = [int(x) for x in start.split(",")]
    end = [int(x) for x in end.split(",")]
    if(start[0] < end[0]): lines.append(start + end)
    else: lines.append(end + start)
lines.sort()
#print(lines)
maxCol = max(sum(lines, [])) + 1

async def countColumn(col):
  count = 0
  hits = [0] * (maxCol)
  for line in lines:
    if line[0] <= col <= line[2]:
      if line[0] == line[2]: #verticle
        start = min(line[1], line[3])
        end = max(line[1], line[3])
        for row in range(start, end + 1):
          hits[row] += 1
      elif line[1] == line[3]: #horizontal
        hits[line[1]] += 1
      else: #diagonal
        x = math.copysign(col - line[0], line[3] - line[1])
        y = int(line[1] + x)
        hits[y] += 1
  
  for x in hits: #count up hits
    if x > 1: count += 1
  return count

async def main():
  coroutines = [countColumn(col) for col in range(maxCol)]
  completed, pending = await asyncio.wait(coroutines)
  count = 0
  for item in completed:
    count += item.result()
  print(count)

if __name__ == '__main__': 
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main())
    finally:
        event_loop.close()