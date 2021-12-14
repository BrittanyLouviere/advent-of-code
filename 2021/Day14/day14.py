#!/usr/bin/python3
import os
from math import ceil

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

polymer = ""
rules = {}
with open(input, 'r') as f:
  polymer = f.readline().strip()
  f.readline()
  for line in f.readlines():
    pair, insert = line.strip().split(" -> ")
    rules[pair] = insert

pairs = {}
for i in range(1, len(polymer)):
  pair = polymer[i-1 : i+1]
  count = pairs.get(pair, 0)
  pairs[pair] = count + 1

steps = 40
for step in range(steps):
  p = {}
  for pair, oldCount in pairs.items():
    newChar = rules[pair]
    for newPair in [pair[0] + newChar, newChar + pair[1]]:
      count = p.get(newPair, 0)
      p[newPair] = count + oldCount
  pairs = p

charCounts = {}
for pair, pairCount in pairs.items():
  for char in pair:
    oldCount = charCounts.get(char, 0)
    charCounts[char] = oldCount + pairCount

for char, count in charCounts.items():
  charCounts[char] = int(ceil(count/2))
if polymer[0] == polymer[-1]:
  charCounts[polymer[0]] += 1

print(max(charCounts.values()) - min(charCounts.values()))