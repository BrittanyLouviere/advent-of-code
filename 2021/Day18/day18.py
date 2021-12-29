#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

allNumbers = []
allSFNums = []
with open(input, 'r') as f:
  for numStr in f.readlines():
    numStr = numStr.strip()
    tempNumbers = numStr.replace("[", "").replace("]", "").split(",")
    for num in tempNumbers:
      digits = len(num)
      i = numStr.index(num)
      numStr = numStr[:i] + "#" + numStr[i+digits:]
    allSFNums.append(numStr)
    allNumbers.append(list(map(int, tempNumbers)))

def sFNumToStr(numbers: list(), sfNum: str) -> str:
  for num in numbers:
    sfNum = sfNum.replace("#", str(num), 1)
  return(sfNum)

def addSFNumbers(nums: list(), sfNums: list()):
  sfNum = ""
  numbers = []

  for addSFIndex in range(len(sfNums)):
    if addSFIndex == 0:
      sfNum += sfNums[addSFIndex]
    else:
      sfNum = "[{},{}]".format(sfNum, sfNums[addSFIndex])
    numbers.extend(nums[addSFIndex])

    stillReducing = True
    while stillReducing:
      stillReducing = False
      
      #check for explodes
      exploded = True
      while exploded:
        exploded = False
        depth = numIndex = 0
        for index in range(len(sfNum)):
          current = sfNum[index]
          if current == "[":
            depth += 1
          elif current == "]":
            depth -= 1
          elif depth > 4 and current == "#" and sfNum[index+2] == "#":
            # explode!
            if numIndex > 0:
              numbers[numIndex-1] += numbers[numIndex]
            if numIndex+2 < len(numbers):
              numbers[numIndex+2] += numbers[numIndex+1]
            numbers[numIndex] = 0
            numbers.pop(numIndex+1)
            sfNum = sfNum[:index-1] + "#" + sfNum[index+4:]
            depth -= 1
            exploded = True
            break
          elif current == "#":
            numIndex += 1

      #check for splits
      for index in range(len(numbers)):
        num = numbers[index]
        if num > 9:
          # split!
          a = num // 2
          b = num - a
          numbers = numbers[:index] + [a, b] + numbers[index+1:]
          numCounter = 0
          for i in range(len(sfNum)):
            char = sfNum[i]
            if char == "#": 
              if numCounter == index:
                sfNum = sfNum[:i] + "[#,#]" + sfNum[i+1:]
                stillReducing = True
                break
              else:
                numCounter += 1
          break

  # find magnitude
  while len(sfNum) > 1:
    numCounter = 0
    for i in range(len(sfNum)):
      char = sfNum[i]
      if char == "#": 
        if sfNum[i+2] == "#":
          numbers[numCounter] = 3*numbers[numCounter] + 2*numbers[numCounter+1]
          numbers.pop(numCounter+1)
          sfNum = sfNum[:i-1] + "#" + sfNum[i+4:]
          break
        else:
          numCounter += 1
  return(numbers[0])

print("Part 1: ", addSFNumbers(allNumbers, allSFNums))

magnitudes = []
for i in range(len(allNumbers)):
  for j in range(len(allNumbers)):
    if i == j: continue
    x = [allNumbers[i], allNumbers[j]]
    y = [allSFNums[i], allSFNums[j]]
    #print(numberToStr(x[0], y[0]))
    #print(numberToStr(x[1], y[1]))
    magnitudes.append(addSFNumbers(x, y))

print("Part 2: ", max(magnitudes))