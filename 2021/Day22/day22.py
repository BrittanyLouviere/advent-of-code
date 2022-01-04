#!/usr/bin/python3
import os
from queue import SimpleQueue

root = os.path.dirname(os.path.abspath(__file__))
example1 = os.path.join(root, 'Example1.txt')
example2 = os.path.join(root, 'Example2.txt')
example3 = os.path.join(root, 'Example3.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

instructions = SimpleQueue()
with open(input, 'r') as f:
  for line in f.readlines():
    order, cuboid = line.strip().split()
    x, y, z = cuboid.split(",")
    xMin, xMax = list(map(int, x[2:].split("..")))
    yMin, yMax = list(map(int, y[2:].split("..")))
    zMin, zMax = list(map(int, z[2:].split("..")))
    instructions.put((order == "on", ((xMin, xMax), (yMin, yMax), (zMin, zMax))))

def intersects (cuboid1, cuboid2):
  for axis in range(3):
    if ((cuboid1[axis][0] < cuboid2[axis][0] and cuboid1[axis][1] < cuboid2[axis][0]) 
    or  (cuboid1[axis][0] > cuboid2[axis][1] and cuboid1[axis][1] > cuboid2[axis][1])):
      return False
  return True

# is cuboid1 entirely inside cuboid2?
def containsCuboid (cuboid1, cuboid2):
  for axis in range(3):
    if not (cuboid2[axis][0] <= cuboid1[axis][0] <= cuboid2[axis][1]
        and cuboid2[axis][0] <= cuboid1[axis][1] <= cuboid2[axis][1]
    ):
      return False
  return True

# restrict defaults to None which means no resitrictions
def cubesInCuboid (cuboid, restrict = None):
  cubes = 1
  for axis in range(3):
    minNum, maxNum = cuboid[axis]
    if restrict != None:
      if minNum < restrict * -1 and maxNum < restrict * -1 or minNum > restrict and maxNum > restrict:
        return 0
      minNum = max(minNum, restrict * -1)
      maxNum = min(maxNum, restrict)
    cubes *= abs(minNum - maxNum) + 1
  return cubes

cuboids = []
while not instructions.empty():
  state, instCuboid = instructions.get()
  newCuboidList = []
  if state: # add new cuboid if on
    newCuboidList.append(instCuboid)

  for currCuboid in cuboids:
    if not intersects(currCuboid, instCuboid):
      # no intersection, cuboid doesn't need division
      newCuboidList.append(currCuboid)
    elif containsCuboid(currCuboid, instCuboid):
      # cuboid is entirely covered, remove it from consideration
      pass
    else:
      # divide currCuboid up
      template = [currCuboid[0], currCuboid[1], currCuboid[2]]
      for axis in range(3):
        currAxis = currCuboid[axis]
        instAxis = instCuboid[axis]
        if ( (currAxis[0] < instAxis[0] and currAxis[1] < instAxis[0])
          or (currAxis[0] > instAxis[1] and currAxis[1] > instAxis[1])
          or (currAxis[0] >= instAxis[0] and currAxis[1] <= instAxis[1])
        ): 
          template[axis] = currAxis
        else:
          q = []
          divCuboids = []
          #first division
          if currAxis[0] < instAxis[0]:
            template[axis] = (currAxis[0], instAxis[0] - 1)
            divCuboids.append(tuple(template))
            q.append(instAxis[0])
          else:
            q.append(currAxis[0])
          
          #second division
          if currAxis[1] > instAxis[1]:
            template[axis] = (instAxis[1] + 1, currAxis[1])
            divCuboids.append(tuple(template))
            q.append(instAxis[1])
          else:
            q.append(currAxis[1])
          
          #third division
          template[axis] = tuple(q)

          for c in divCuboids:
            if containsCuboid(c, currCuboid) and not intersects(c, instCuboid):
              newCuboidList.append(c)
  cuboids = newCuboidList

# count cubes in each cuboid
part1 = 0
part2 = 0
for cuboid in cuboids:
  part1 += cubesInCuboid(cuboid, 50)
  part2 += cubesInCuboid(cuboid)

print("Part 1: ", part1)
print("Part 2: ", part2)