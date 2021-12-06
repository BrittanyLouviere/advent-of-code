#!/usr/bin/python3
import os

def part1(input):
  file = open(input, 'r')
  bits = []

  for line in file:
    input = line.strip()
    if (len(bits) == 0): #initialize bits array if not already
      bits = [0] * len(input)
    for i in range(0, len(input)): #+1 if '1', -1 if '0'
      bits[i] = bits[i] + 1 - 2 * int(input[i] == '1')

  gamma = "" #most common
  epsilon = "" #least common
  for bit in bits:
    gamma += str(int(bit > 0))
    epsilon += str(int(bit < 0))

  print(int(gamma, 2) * int(epsilon, 2))

def part2(input):
  o2 = []
  co2 = []
  all = []
  with open(input, 'r') as f:
    for x in f.readlines():
      all.append(x.strip())
  
  firstCol = [row[0] for row in all]
  zeros = firstCol.count('0')
  ones = firstCol.count('1')
  mostCommon = ''
  if zeros > ones:
    mostCommon = '0'
  else:
    mostCommon = '1'

  while(len(all) > 0):
    if (all[0][0] == mostCommon):
      o2.append(all.pop(0))
    else:
      co2.append(all.pop(0))

  for col in range(1, len(o2[0])):
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
  
  for col in range(1, len(co2[0])):
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

all = []
def getInput(input):
  with open(input, 'r') as f:
    for x in f.readlines():
      all.append(list(x.strip()))

def part1_2():
  gamma = ""
  epsilon = ""
  for i in range(0, len(all[0])):
    colBits = [row[i] for row in all]
    zeros = colBits.count('0')
    gamma += str(int(zeros < len(all) - zeros))
  
  for bit in gamma:
    epsilon += str(int(bit == '0'))

  print(int(gamma, 2) * int(epsilon, 2))

def part2_2():
  firstCol = [row[0] for row in all]
  zeros = firstCol.count('0')
  checkBit = str(int(zeros < len(all) - zeros))

  o2 = []
  co2 = []
  for i in range(0, len(all)):
    if (all[i][0] == checkBit):
      o2.append(i)
    else:
      co2.append(i)
  
  while(len(o2) > 1):
    for i in range(1, len(all[0])):
      colBits = [all[x][i] for x in o2]
      zeros = firstCol.count('0')
      checkBit = str(int(zeros < len(colBits) - zeros))
      for i in range(1, len(colBits)):
        index = len(colBits)-i
        if (colBits[index] != checkBit and len(o2) != 1):
          del o2[index]
  print(o2[0])



root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

#part1(bigboy)

#getInput(example)
#part1_2()
part1(input)