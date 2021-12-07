#!/usr/bin/python3
import os
import statistics as stats

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

crabs = []
with open(input, 'r') as f:
  for i in f.readline().split(','):
    crabs.append(int(i))

def part1():
  leastFuel = None
  for x in range(max(crabs)):
    fuel = 0
    for crab in crabs:
      fuel += abs(crab - x)
    if leastFuel == None or leastFuel > fuel:
      leastFuel = fuel
  print("part 1: ", leastFuel)

def part1Med():
  x = int(stats.median(crabs))
  fuel = 0
  for crab in crabs:
    fuel += abs(crab - x)
  print("part 1: ", fuel)

def part2():
  leastFuel = None
  for x in range(max(crabs)):
    fuel = 0
    for crab in crabs:
      steps = abs(crab - x) + 1
      for i in range(steps):
        fuel += i
    if leastFuel == None or leastFuel > fuel:
      leastFuel = fuel
  print("part 2: ", leastFuel)

def part2Mean():
  x = int(stats.mean(crabs))
  fuel = 0
  for crab in crabs:
    steps = abs(crab - x) + 1
    for i in range(steps):
      fuel += i
  print("part 2: ", fuel)

#part1()
part1Med()
#part2()
part2Mean()