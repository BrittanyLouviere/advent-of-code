#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example1 = os.path.join(root, 'Example1.txt')
example2 = os.path.join(root, 'Example2.txt')
example3 = os.path.join(root, 'Example3.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

instructions = []
with open(example3, 'r') as f:
  for line in f.readlines():
    order, area = line.strip().split()
    x, y, z = area.split(",")
    xMin, xMax = list(map(int, x[2:].split("..")))
    yMin, yMax = list(map(int, y[2:].split("..")))
    zMin, zMax = list(map(int, z[2:].split("..")))
    instructions.append((order == "on", ((xMin, xMax), (yMin, yMax), (zMin, zMax))))

cubes = set()
for order, area in instructions:
  for x in range(area[0][0], area[0][1] + 1):
    for y in range(area[1][0], area[1][1] + 1):
      for z in range(area[2][0], area[2][1] + 1):
        if order:
          cubes.add((x, y,z))
        else:
          try: cubes.remove((x, y,z))
          except: pass

print("Part 1: ", len(cubes))