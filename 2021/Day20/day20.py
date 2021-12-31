#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

algorithm = ""
image = []
with open(input, 'r') as f:
  algorithm = f.readline().strip()
  f.readline()
  image = list(map(str.strip, f.readlines()))

def padImage (image, padNum, char):
  for row in range(len(image)):
    image[row] = char*padNum + image[row] + char*padNum

  length = len(image[0])
  for _ in range(padNum):
    image.append(char * length)
    image.insert(0, char * length)

#print("\n".join(image) + "\n")
infiniChars = (algorithm[int("0"*9, 2)], algorithm[int("1"*9, 2)])
infiniChar = "."
part1Count = 0
for i in range(50):
  if i == 2:
    part1Count = "".join(image).count("#")
  padImage(image, 2, infiniChar)
  newImage = image.copy()

  for row in range(len(image)):
    for col in range(len(image[0])):
      pixels = ""
      for r in [row-1, row, row+1]:
        if r < 0 or r >= len(image):
          pixels += infiniChar * 3
          continue
        for c in [col-1, col, col+1]:
          if c < 0 or c >= len(image[0]):
            pixels += infiniChar
          else:
            pixels += image[r][c]
      
      binary = pixels.replace(".", "0").replace("#", "1")
      number = int(binary, 2)
      newPixel = algorithm[number]
      newImage[row] = newImage[row][:col] + newPixel + newImage[row][col+1:]
  image = newImage
  infiniChar = infiniChars[infiniChar == "#"]
  #print("\n".join(image) + "\n")

part2Count = "".join(image).count("#")
print("Part 1: ", part1Count)
print("Part 2: ", part2Count)