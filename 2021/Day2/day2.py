#!/usr/bin/python3
import os

def part1(input):
  depth = 0
  length = 0
  file = open(input, 'r')
  
  for line in file:
    command, number = line.split()
    number = int(number)
    if (command == "forward"): 
      length += number
    elif (command == "down"): 
      depth += number
    elif (command == "up"): 
      depth -= number

  print(depth * length)

def part2(input):
  aim = 0
  depth = 0
  length = 0
  file = open(input, 'r')

  for line in file:
    command, number = line.split()
    number = int(number)
    if (command == "down"): 
      aim += number
    elif (command == "up"): 
      aim -= number
    elif (command == "forward"):
      length += number
      depth += aim * number

  print(depth * length)

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

part1(input)
part2(input)