#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

xMin = xMax = yMin = yMax = 0
with open(input, 'r') as f:
  nums = f.readline()[15:].replace(", y=", "..").split("..")
  xMin = int(nums[0])
  xMax = int(nums[1])
  yMin = int(nums[2])
  yMax = int(nums[3])

initVels = 0
highestYPos = 0

for initX in range(xMax + 1):
  for initY in range(yMin, abs(yMin) + 1):
    velX = initX
    velY = initY
    posX = posY = posYMax = 0
    while posX <= xMax and posY >= yMin:
      posYMax = max(posYMax, posY)
      if posX >= xMin and posY <= yMax:
        initVels += 1
        highestYPos = max(highestYPos, posYMax)
        break
      posX += velX
      posY += velY
      velX = max(velX - 1, 0)
      velY -= 1

print("Part 1: ", highestYPos)
print("Part 2: ", initVels)