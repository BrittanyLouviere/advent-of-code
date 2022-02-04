#!/usr/bin/python3
import os
from math import sqrt

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')

class Beacon:
  coordinates = [0,0,0]

  def __init__(self, x:int, y:int, z:int) -> None:
    self.coordinates = [x, y, z]
  def __eq__(self, __o: object) -> bool:
    return self.coordinates == __o.coordinates
  def __lt__(self, __o: object) -> bool:
    return self.coordinates < __o.coordinates
  def __str__(self) -> str:
    return str(self.coordinates)

  def distance(self, oBeacon) -> float:
    dX = self.coordinates[0] - oBeacon.coordinates[0]
    dY = self.coordinates[1] - oBeacon.coordinates[1]
    dZ = self.coordinates[2] - oBeacon.coordinates[2]
    return sqrt(dX**2 + dY**2 + dZ**2)

class Scanner:
  beacons = []
  beaconDistances = {}

  def __init__(self, beacons:list) -> None:
    self.beacons = beacons
    self.beaconDistances = {}
    for a in range(len(beacons)):
      beaconA = beacons[a]
      for b in range(a+1, len(beacons)):
        beaconB = beacons[b]
        distance = round(beaconA.distance(beaconB))
        beaconSet:list = self.beaconDistances.get(distance, [])
        beaconSet.append((beaconA, beaconB))
        self.beaconDistances[distance] = beaconSet

  def addBeacon(self, newBeacon:Beacon) -> None:
    for beacon in self.beacons:
      distance = round(beacon.distance(newBeacon))
      beaconSet = self.beaconDistances.get(distance, [])
      beaconSet.append((beacon, newBeacon))
      self.beaconDistances[distance] = beaconSet
    self.beacons.append(newBeacon)

def getTransformations (tupleA, tupleB):
  possibleTransformations = []
  beaconA = list(tupleA)
  beaconB = list(tupleB)
  for permutation in [(0, 1, 2),(0, 2, 1),(1, 0, 2),(1, 2, 0),(2, 0, 1),(2, 1, 0)]:
    for orientation in [(1, 1, 1),(1, 1, -1),(1, -1, 1),(1, -1, -1),(-1, 1, 1),(-1, 1, -1),(-1, -1, 1),(-1, -1, -1)]:
      newBeaconB = [
        beaconB[permutation[0]] * orientation[0], 
        beaconB[permutation[1]] * orientation[1], 
        beaconB[permutation[2]] * orientation[2]
      ]
      translation = (beaconA[0] - newBeaconB[0], beaconA[1] - newBeaconB[1], beaconA[2] - newBeaconB[2])
      possibleTransformations.append((permutation, orientation, translation))
  return possibleTransformations

scanners = []
with open(input, 'r') as f:
  f.readline()
  newScanner = []
  for line in f.readlines():
    if "scanner" in line:
      scanners.append(Scanner(newScanner))
      newScanner = []
    elif line.isspace():
      continue
    else:
      x, y, z = list(map(int, line.strip().split(",")))
      newScanner.append(Beacon(x, y, z))
  scanners.append(Scanner(newScanner))

scannerPositions = [(0,0,0)]
beaconMap:Scanner = scanners.pop(0)
while len(scanners) > 0:
  currentScanner:Scanner = scanners.pop(0)

  # get matching distances between two sets
  matchedDistances = beaconMap.beaconDistances.keys() & currentScanner.beaconDistances.keys()
  possibleMatches = {} # (beaconMap, currentScanner): count

  # count up how many possible beacon matches for each matched distance
  for matchedDistance in matchedDistances:
    mapBeacons = beaconMap.beaconDistances[matchedDistance]
    currentBeacons = currentScanner.beaconDistances[matchedDistance]
    for beaconSetA in mapBeacons:
      for beaconSetB in currentBeacons:
        for i in [(0,0), (0,1), (1,0), (1,1)]:
          coords = (tuple(beaconSetA[i[0]].coordinates), tuple(beaconSetB[i[1]].coordinates))
          matchCount = possibleMatches.get(coords, 0)
          possibleMatches[coords] = matchCount + 1

  # get list of possible matches that have a count >= 11
  indices = [i for i, x in enumerate(possibleMatches.values()) if x >= 11]
  possibleMatches = [x for i, x in enumerate(possibleMatches.keys()) if i in indices]

  # count up how many possible transformations for each matched beacon
  possibleTransformations = {}
  for match in possibleMatches:
    transformations = getTransformations(match[0], match[1])
    for transformation in transformations:
      count = possibleTransformations.get(transformation, 0)
      possibleTransformations[transformation] = count + 1

  # get list of possible transformations that have a count >= 12
  indices = [i for i, x in enumerate(possibleTransformations.values()) if x >= 12]
  possibleTransformations = [x for i, x in enumerate(possibleTransformations.keys()) if i in indices]
  if len(possibleTransformations) == 0:
    scanners.append(currentScanner)
  else:
    permutation, orientation, translation = possibleTransformations[0]
    scannerPositions.append(translation)
    for beacon in currentScanner.beacons:
      coords = beacon.coordinates
      x = coords[permutation[0]] * orientation[0] + translation[0]
      y = coords[permutation[1]] * orientation[1] + translation[1]
      z = coords[permutation[2]] * orientation[2] + translation[2]
      newBeacon = Beacon(x, y, z)
      if newBeacon not in beaconMap.beacons:
        beaconMap.addBeacon(newBeacon)

print("Part 1: ", len(beaconMap.beacons))

# find manhattan distance between all scanners
maxDistance = 0
for i in range(len(scannerPositions)):
  scannerA = scannerPositions[i]
  for j in range(i+1, len(scannerPositions)):
    scannerB = scannerPositions[j]
    dx = abs(scannerA[0] - scannerB[0])
    dy = abs(scannerA[1] - scannerB[1])
    dz = abs(scannerA[2] - scannerB[2])
    maxDistance = max(maxDistance, dx + dy + dz)
print("Part 2: ", maxDistance)