#!/usr/bin/python3
import os
from queue import SimpleQueue

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
  conversion = []
  for beaconAId in range(len(scanner)):
    beaconA = scanner[beaconAId]
    conversion.append([])
    for beaconBId in range(len(scanner)):
      beaconB = scanner[beaconBId]
      conversion[beaconAId].append([])
      for coord in range(3):
        conversion[beaconAId][beaconBId].append(beaconA[coord] - beaconB[coord])
  beaconRelativePositions.put(conversion)

def coordsAreMatch (coordA: list(), coordB: list()) -> bool:
  absA = list(map(abs, coordA))
  absB = list(map(abs, coordB))
  matchCount = 0
  for coord in absA:
    if coord in absB:
      matchCount += 1
  return matchCount == len(coordA)

def findMatchingBeacons (beaconSetA: list(), beaconSetB: list()) -> tuple():
  for beaconA in beaconSetA:
    for beaconB in beaconSetB:
      matches = 0
      coordMatches = [None] * len(beaconB)
      for coordBId in range(len(beaconB)):
        coordB = beaconB[coordBId]
        for coordAId in range(len(beaconA)):
          coordA = beaconA[coordAId]
          if coordAId in coordMatches: continue
          if coordsAreMatch(coordA, coordB):
            matches += 1
            coordMatches[coordBId] = coordAId
            break
      if matches > 11:
        return (coordMatches)
  return None

def convertBeacons (conversion: list(), beaconSet: list()) -> list():
  newBeaconSet = []
  for beacon in beaconSet:
    newBeacon = []
    for coords in beacon:
      newCoords = [None, None, None]
      for i in range(3):
        con = conversion[i]
        coord = coords[i]
        if con < 0:
          con *= -1
          coord *= -1
        newCoords[con] = coord
      newBeacon.append(newCoords)
    newBeaconSet.append(newBeacon)
  return newBeaconSet

def getUniqueBeacons ():
  pass

beacons: list() = beaconRelativePositions.get()
while not beaconRelativePositions.empty():
  beaconSet = beaconRelativePositions.get()
  foundBeacons = []
  newBeacons = []
  result = findMatchingBeacons(beacons, beaconSet)
  if result is None:
    beaconRelativePositions.put(beaconSet)
  else:
    conversion = []
    for coord in result[1]:
      try:
        conversion.append(result[0].index(coord))
      except:
        conversion.append(result[0].index(coord * -1) * -1)
    beacons.extend(convertBeacons(conversion, beaconSet))

