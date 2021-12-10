#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

def solution(daysToRun, filePath):
  maxTimer = 8
  resetTimer = 6
  fish = [0] * (maxTimer + 1)
  with open(filePath, 'r') as f:
    for x in f.readline().split(','):
      fish[int(x)] += 1

  for day in range(daysToRun):
    newFishArr = [0] * (maxTimer + 1)
    for i in range(maxTimer + 1):
      if i == 0:
        newFishArr[resetTimer] += fish[i]
        newFishArr[maxTimer] += fish[i]
      else:
        newFishArr[i-1] += fish[i]
    fish = newFishArr

    #print("Day ", day)

  #print(fish)
  return(sum(fish))

print("Part 1 example: ", solution(80, example))
print("Part 1 solution: ", solution(80, input))
print("Part 1 example: ", solution(256, example))
print("Part 1 solution: ", solution(256, input))
#print("Part 2 Big Boy: ", solution(9999999, example))