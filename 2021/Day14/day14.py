#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

polymer = ""
rules = {}
with open(example, 'r') as f:
  polymer = f.readline().strip()
  f.readline()
  for line in f.readlines():
    pair, insert = line.strip().split(" -> ")
    rules[pair] = insert

steps = 40
for step in range(steps):
  p = ""
  for i in range(len(polymer)):
    pair = polymer[i:i+2]
    mid = rules.get(pair, "")
    p += pair[0] + mid
  polymer = p

counts = []
for char in set(polymer):
  counts.append(polymer.count(char))
print(max(counts) - min(counts))