#!/usr/bin/python3
import os
import numpy as np

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

all = []
with open(example, 'r') as f:
  for x in f.readlines():
    all.append(list(x.strip()))
  all = np.array(all)

zeros = np.count_nonzero(all == '0', axis = 0)
ones = np.count_nonzero(all == '1', axis = 0)
x = zeros - ones < 0
gamma = ''.join((x).astype(int).astype(str))
epsilon = ''.join((np.invert(x)).astype(int).astype(str))
powerConsumption = int(gamma, 2) * int(epsilon, 2)
print("part 1: ", powerConsumption)

o2List = []
co2List = []
o2 = ''
co2 = ''
x = x[0]
o2 += str(int(x))
co2 += str(int(not x))
#split all array into the o2 and co2 lists (remove first column?)

print(all)
all.sort(axis = 0)
print(all)