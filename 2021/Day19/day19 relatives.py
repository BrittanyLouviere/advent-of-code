#!/usr/bin/python3
import os

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
beaconRelativePositions = [] * len(scanners)
for scannerId in range(len(scanners)):
  scanner = scanners[scannerId]
  beaconRelativePositions.append([])
  for beaconAId in range(len(scanner)):
    beaconA = scanner[beaconAId]
    beaconRelativePositions[scannerId].append([])
    for beaconBId in range(len(scanner)):
      beaconB = scanner[beaconBId]
      beaconRelativePositions[scannerId][beaconAId].append([])
      for coord in range(3):
        beaconRelativePositions[scannerId][beaconAId][beaconBId].append(beaconA[coord] - beaconB[coord])

# scannerPositions holds the coord of this scanner relative to the scannerId deonoted in scannerRelativeTo
scannerPositions = [None] * len(scanners)
scannerPositions[0] = [0,0]
scannerRelativeTo = [None] * len(scanners)
scannerRelativeTo[0] = 0

for scannerAId in range(len(beaconRelativePositions)):
  scannerA = beaconRelativePositions[scannerAId]
  for scannerBId in range(len(beaconRelativePositions)):
    if scannerRelativeTo[scannerBId] != None: continue
    if scannerAId == scannerBId: continue # skip if its the same scanner
    scannerB = beaconRelativePositions[scannerBId]
    #print("A: {}, B: {}".format(scannerAId, scannerBId))
    for beaconA in scannerA:
      if scannerRelativeTo[scannerBId] != None: break
      for beaconB in scannerB:
        if scannerRelativeTo[scannerBId] != None: break
        beaconMatches = 0
        for relativeBeaconA in beaconA:
          if scannerRelativeTo[scannerBId] != None: break
          for relativeBeaconB in beaconB:
            if scannerRelativeTo[scannerBId] != None: break
            absRelB = list(map(abs, relativeBeaconB))
            coordMatches = 0
            for coord in range(3):
              if abs(relativeBeaconA[coord]) in absRelB:
                coordMatches += 1
            if coordMatches > 2:
              beaconMatches += 1
            if beaconMatches > 11:
              if scannerRelativeTo[scannerBId] == None:
                scannerRelativeTo[scannerBId] = scannerBId
              else:
                scannerRelativeTo[scannerAId] = scannerAId
x = 0