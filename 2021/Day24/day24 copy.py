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
  inputs = inputStr.split(",")
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

#############################################################################################
# Trying to go front to back but wouldn't that end with checking every possible combo again?
#############################################################################################

# find model numbers
first = True
results = [["", 0]]
for inst in instructionSets:
  if not first:
    inst = [['inp', 'z']] + inst
  first = False
  results.append([])
  for oldNum, oldZ in results[-2]:
    for num in range(1, 10):
      z = runInstructions(inst, ",".join(str(oldZ), str(num), oldNum))["z"]
      results[-1].append((str(num), z))


# double check model numbers
for _, numbers in results.items():
  z = runInstructions(instructions, numbers)["z"]
  q = 0