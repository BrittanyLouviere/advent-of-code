#!/usr/bin/python3
import os
from queue import SimpleQueue
import numpy as np

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

scanners = []
with open(example, 'r') as f:
  scannerNum = -1
  for line in f.readlines():
    line = line.strip()
    if "---" in line:
      scannerNum += 1
      scanners.append([])
    elif len(line) > 0:
      coord = list(map(int, line.split(",")))
      scanners[scannerNum].append(coord)

# position of beacons relative to each other
beaconRelativePositions = SimpleQueue()
for scannerId in range(len(scanners)):
  scanner = scanners[scannerId]
  conversion = np.empty((len(scanner), len(scanner), len(scanner[0])), int)
  for beaconAId in range(len(scanner)):
    beaconA = scanner[beaconAId]
    for beaconBId in range(len(scanner)):
      beaconB = scanner[beaconBId]
      for coord in range(3):
        conversion[beaconAId][beaconBId][coord] = beaconA[coord] - beaconB[coord]
  beaconRelativePositions.put(conversion)

def findMatchingBeacons (beaconSetA: list(), beaconSetB: list()) -> tuple():
  permutations = [
    [0,1,2],
    [0,2,1],
    [1,2,0],
    [2,1,0],
    [1,0,2],
    [2,0,1]
  ]
  orientations = [
    [ 1, 1, 1],
    [ 1, 1,-1],
    [ 1,-1, 1],
    [ 1,-1,-1],
    [-1, 1, 1],
    [-1, 1,-1],
    [-1,-1, 1],
    [-1,-1,-1]
  ]
  newdtype={'names':['f{}'.format(i) for i in range(3)], 'formats':3 * [np.int64]}

  for beaconB in beaconSetB:
    for perm in permutations:
      permutedB = beaconB[:, perm]
      for ori in orientations:
        orientedB = np.ascontiguousarray(permutedB * ori)
        for beaconA in beaconSetA:
          #intersection = np.intersect1d(beaconA.view(newdtype), orientedB.view(newdtype)).view(np.int64).reshape(-1, 3)
          matches = (orientedB[:,None]==beaconA).any((1, -1))
          if np.count_nonzero(matches) > 11:
            #union = np.union1d(beaconA.view(newdtype), orientedB.view(newdtype)).view(np.int64).reshape(-1, 3)
            x = np.where(matches) * orientedB
            #a = []
            #myIterator = iter(range(5, 100))
            #g = np.where(matches, 1, next(myIterator))
            #for x in orientedB:
            #  q = (beaconA==x).any(1)
            #  y = np.where(q, np.where(q), None)
            #  a.append(y)
            return (matches, beaconA, orientedB)
  return None

def convertBeacons (matches: list(), beaconA: list(), beaconB: list()) -> list():
  newBeacon = []
  np.union1d
  return newBeacon

def getUniqueBeacons ():
  pass

beacons: list() = beaconRelativePositions.get()
while not beaconRelativePositions.empty():
  beaconSet = beaconRelativePositions.get()
  result = findMatchingBeacons(beacons, beaconSet)
  if result is None:
    beaconRelativePositions.put(beaconSet)
  else:
    conversion = convertBeacons(result[0], result[1], result[2])