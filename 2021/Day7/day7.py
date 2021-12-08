#!/usr/bin/python3
import os
import posixpath
import statistics as stats

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

#key: position, value: # of crabs
crabs = {}
mean = 0
median = 0
with open(bigboy, 'r') as f:
  input = list(map(int, f.readline().split(',')))
  median = int(stats.median(input))
  mean = int(stats.mean(input))
  for pos in input:
    if pos in crabs:
      crabs[pos] += 1
    else:
      crabs[pos] = 1

#part 1
fuel = 0
for pos in crabs:
  fuel += abs(pos - median) * crabs[pos]
print("Part 1: ", fuel)

#part 2
#key: target position, value: total fuel cost
targets = {mean: 0, mean + 1: 0, mean - 1: 0}
maxSteps = 0

maxPos = max(crabs)
minPos = min(crabs)
for target in targets:
  maxSteps = max(maxSteps, abs(target - maxPos), abs(target - minPos))

fuelCost = 0
for steps in range(1, maxSteps + 1):
  fuelCost += steps
  for target in targets:
    plus = target + steps
    minus = target - steps
    if plus in crabs:
      targets[target] += fuelCost * crabs[plus]
    if minus in crabs:
      targets[target] += fuelCost * crabs[minus]

print("Part 2: ", min(targets.values()))