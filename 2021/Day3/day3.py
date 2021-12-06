#!/usr/bin/python3
import os

def part1(input):
  file = open(input, 'r')
  bits = []

  for line in file:
    input = list(line.strip())
    for i in range(0, len(input)):
      if (i >= len(bits)):
        bits.append([0, 0])
      
      if (input[i] == '0'):
        bits[i][0] += 1
      else:
        bits[i][1] += 1

  gamma = "" #most common
  epsilon = "" #least common
  for bit in bits:
    if bit[0] > bit[1]:
      gamma += "0"
      epsilon += "1"
    else :
      gamma += "1"
      epsilon += "0"

  answer = int(gamma, 2) * int(epsilon, 2)
  print("answer: ", answer)

def part2(input):
  o2 = []
  co2 = []
  with open(input, 'r') as f:
    for x in f.readlines():
      o2.append(list(x.strip()))
      co2.append(list(x.strip()))

  for col in range(0, len(o2[0])):
    toDel = []
    colBits = [row[col] for row in o2]
    zeros = colBits.count('0')
    ones = colBits.count('1')
    mostCommon = ''
    if zeros > ones:
      mostCommon = '0'
    else:
      mostCommon = '1'

    for row in range(0, len(o2)):
      if (mostCommon != o2[row][col]):
        toDel.insert(0, row)

    for i in toDel:
      del o2[i]
    if (len(o2) == 1):
      break

  for col in range(0, len(co2[0])):
    toDel = []
    colBits = [row[col] for row in co2]
    zeros = colBits.count('0')
    ones = colBits.count('1')
    mostCommon = ''
    if zeros > ones:
      mostCommon = '0'
    else:
      mostCommon = '1'

    for row in range(0, len(co2)):
      if (mostCommon == co2[row][col]):
        toDel.insert(0, row)
    
    x = 2
    for i in toDel:
      del co2[i]
    if (len(co2) == 1):
      break

  print(int("".join(o2[0]), 2) * int("".join(co2[0]), 2))



root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

part1(input)
part2(input)