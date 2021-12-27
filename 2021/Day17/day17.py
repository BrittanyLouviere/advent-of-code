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

xVelDict = {}
for xVelStart in range(xMax):
  xVel = xVelStart
  xPos = 0
  steps = 0
  while xPos < xMax:
    if xPos >= xMin:
      if steps not in xVelDict:
        xVelDict[steps] = []
      xVelDict[steps].append(xVelStart)
    xPos += xVel
    xVel -= 1
    if xVel < 0: break
    steps += 1

highestYPos = 0
yVelDict = {}
yVelStart = yMax
while yVelStart < abs(yMin):
  yPosMax = 0
  yVel = yVelStart
  yPos = 0
  steps = 0
  while yPos >= yMin:
    if yPos > yPosMax:
      yPosMax = yPos
    if yPos <= yMax:
      if steps not in yVelDict:
        yVelDict[steps] = []
      yVelDict[steps].append(yVelStart)
      if steps >= min(xVelDict):
        if yPosMax > highestYPos:
          highestYPos = yPosMax
        break
    yPos += yVel
    yVel -= 1
    steps += 1
  yVelStart += 1

print("Part 1: ", highestYPos)