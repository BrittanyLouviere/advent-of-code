#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

part1count = 0
part2count = 0
with open(input, 'r') as f:
  for line in f.readlines():
    decode = [""] * 10
    input, output = line.strip().split(" | ")
    fiveSegs = []
    sixSegs = []
    for num in input.split(): #decode uniques and split up five and six segment numbers
      length = len(num)
      if length == 2: #it's a 1
        decode[1] = "".join(sorted(num))
      elif length == 4: #it's a 4
        decode[4] = "".join(sorted(num))
      elif length == 3: #it's a 7
        decode[7] = "".join(sorted(num))
      elif length == 7: #it's a 8
        decode[8] = "".join(sorted(num))
      elif length == 5: #could be 2, 3, or 5
        fiveSegs.append("".join(sorted(num)))
      elif length == 6: #could be 0, 6, or 9
        sixSegs.append("".join(sorted(num)))
    
    fourMinusOne = decode[4]
    for char in decode[1]:
      fourMinusOne = fourMinusOne.replace(char, "")

    for num in fiveSegs: #decode five segment numbers
      if all([characters in num for characters in decode[1]]): #it's 3
        decode[3] = num
      elif all([characters in num for characters in fourMinusOne]): #it's 5
        decode[5] = num
      else: #it's 2
        decode[2] = num

    for num in sixSegs: #decode six segment numbers
      if all([characters in num for characters in decode[4]]): #it's 9
        decode[9] = num
      elif all([characters in num for characters in fourMinusOne]): #it's 6
        decode[6] = num
      else: #it's 0
        decode[0] = num

    decodedOutput = ""
    for num in  output.split():
      length = len(num)
      if length == 2 or length == 4 or length == 3 or length == 7:
        part1count += 1
      decodedOutput += str(decode.index("".join(sorted(num))))
    part2count += int(decodedOutput)

print("Part 1: ", part1count)
print("Part 2: ", part2count)