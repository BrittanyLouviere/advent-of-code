#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
inputData = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

instructions = []
with open(inputData, 'r') as f:
  for i in f.readlines():
    instructions.append(i.strip().split())

def runInstructions(instructions, inputStr = None):
  inputs = list(reversed(inputStr.split(",")))
  alu = {
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0
  } 
  for instruction in instructions:
    # parse instruction
    if len(instruction) == 2:
      command, var1 = instruction
      if inputStr == None:
        print(alu["z"])
        var2 = input("Enter a number: ")
      else:
        var2 = inputs.pop()
    else:
      command, var1, var2 = instruction
    # execute instructions
    try: var2 = int(var2)
    except: var2 = alu[var2]
    if command == "inp":
      alu[var1] = var2
    elif command == "add":
      alu[var1] = alu[var1] + var2
    elif command == "mul":
      alu[var1] = alu[var1] * var2
    elif command == "div":
      alu[var1] = alu[var1] // var2
    elif command == "mod":
      alu[var1] = alu[var1] % var2
    elif command == "eql":
      alu[var1] = int(alu[var1] == var2)
  return alu

# seperate instuctions by input
instructionSets = []
for inst in instructions:
  if inst[0] == "inp":
    instructionSets.append([])
  instructionSets[-1].append(inst)

# find model numbers
# z : num
prevResults = {0: ''}
for inst in instructionSets:
  inst = [['inp', 'z']] + inst
  currResults = {}
  for prevZ, prevNum in prevResults.items():
    for num in range(1, 10):
      z = runInstructions(inst, ",".join([str(prevZ), str(num)]))["z"]
      newNum = prevNum + str(num)
      oldNum = currResults.get(z, None)
      # if oldNum is None or int(newNum) > int(oldNum): # for part 1
      if oldNum is None or int(newNum) < int(oldNum): # for part 2
        currResults[z] = newNum
  
  zSet = set(currResults.keys())
  maxZ = max(zSet) / 26

  lowerResults = [(zs, nums) for zs, nums in currResults.items() if zs < maxZ]
  if len(lowerResults) > 0:
    newResults = {}
    for zs, nums in lowerResults:
      newResults[zs] = nums
    currResults = newResults
  prevResults = currResults

# for part 1
# maxNum = max(currResults.values())
# print(maxNum)

# for part 2
minNum = min(currResults.values())
print(minNum)