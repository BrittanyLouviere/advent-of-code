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
results = {0: None}
for instCount in reversed(range(0, len(instructionSets))):
  inst = [['inp', 'z']] + instructionSets[instCount]
  newResults = {}
  for goal, oldNums in results.items():
    z = -1
    timer = 0
    foundNewResult = False
    while timer < 10 and (instCount != 0 or z != 0):
#    while z < 1000 and (instCount != 0 or z != 0):
      z += 1
      for i in [1, -1]:
        zTest = z * i
        for newNum in range(1, 10):
          inputStr = str(newNum)
          if oldNums != None: inputStr = inputStr + "," + oldNums
          newZ = runInstructions(inst, str(zTest) + "," + str(newNum))["z"]
          if newZ == goal:
            oldStr = newResults.get(zTest, None)
            if oldStr == None or int(oldStr.replace(",", "")) < int(inputStr.replace(",", "")):
              newResults[zTest] = inputStr
            foundNewResult = True
      timer += foundNewResult
  results = newResults

##########################################################
# It takes a loooooong time to run
##########################################################

# double check model numbers
for _, numbers in results.items():
  z = runInstructions(instructions, numbers)["z"]
  q = 0