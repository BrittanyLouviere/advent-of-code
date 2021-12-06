#!/usr/bin/python3
import os

def part1(input):
  depths = []
  with open(input, 'r') as f:
    depths = list(map(int, f.readlines()))

  decreaseCount = 0
  for i in range(len(depths)-1):
    if (depths[i] < depths[i+1]):
      decreaseCount += 1

  print(decreaseCount)

def part1_2(input):
  file = open(input, 'r')
  decreaseCount = -1
  prev = 0

  for line in file:
    decreaseCount += prev < int(line)
    prev = int(line)

  print(decreaseCount)


def part2(input):
  depths = []
  with open(input, 'r') as f:
    depths = list(map(int, f.readlines()))

  decreaseCount = 0
  for i in range(len(depths)-3):
    sum1 = depths[i] + depths[i+1] + depths[i+2]
    sum2 = depths[i+1] + depths[i+2] + depths[i+3]
    if (sum1 < sum2):
      decreaseCount += 1

  print(decreaseCount)

def part2_2(input):
  file = open(input, 'r')
  decreaseCount = -1
  nums = []

  for line in file:
    #num
    decreaseCount += prev < int(line)
    prev = int(line)

  print(decreaseCount)

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

part1(input)
#part1_2(input)
part2(input)