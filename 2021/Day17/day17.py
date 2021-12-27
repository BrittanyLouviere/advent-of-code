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

# key: steps, val: array of initial y velocities
yHits = {}
yMaxs = {}
for initY in range(yMin, abs(yMin) + 1):
  velY = initY
  posY = posYMax = step = 0
  while posY >= yMin:
    posYMax = max(posYMax, posY)
    if posY <= yMax:
      if step not in yHits:
        yHits[step] = []
      yHits[step].append(initY)
      yMaxs[step] = max(yMaxs.get(step, 0), posYMax)
    posY += velY
    velY -= 1
    step += 1

initVels = 0
highestYPos = 0

xStart = 0
test = 0
while test < xMin:
  test += xStart
  xStart += 1
xStart -= 1
maxStep = max(yHits)

for initX in range(xStart, xMax + 1):
  velX = initX
  posX = step = 0
  initYs = set()
  while posX <= xMax and step <= maxStep:
    if posX >= xMin:
      highestYPos = max(highestYPos, yMaxs.get(step, 0))
      for initY in yHits.get(step, []):
        initYs.add(initY)
    posX += velX
    velX = max(velX - 1, 0)
    step += 1
  initVels += len(initYs)

print("Part 1: ", highestYPos)
print("Part 2: ", initVels)