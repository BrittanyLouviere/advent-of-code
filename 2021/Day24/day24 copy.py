#!/usr/bin/python3
import os
from unittest import result

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

results = [[] for _ in range(14)]
for i in range(0,10):
  for j in range(len(instructionSets)):
    results[j].append(runInstructions(instructionSets[j], str(i))["z"])

#############################################################################################
# Trying to go front to back but wouldn't that end with checking every possible combo again?
# Takes a long time to run...
#############################################################################################

# find model numbers
first = True
results = [{0: []}]
for inst in instructionSets:
  inst = [['inp', 'z']] + inst
  results.append({})
  for prevZ, prevNum in results[-2].items():
    for num in range(1, 10):
      z = runInstructions(inst, ",".join([str(prevZ), str(num)]))["z"]
      oldNum = results[-1].get(z, [-1])[0]
      if oldNum < num:
        results[-1][z] = [num] + prevNum


# double check model numbers
for finalZ, numbers in results[-1].items():
  z = runInstructions(instructions, str(numbers)[1:-1].replace(" ", ""))["z"]
  if z == finalZ:
    q = 0
  else:
    q = 0