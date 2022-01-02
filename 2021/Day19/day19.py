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

# scannerPositions holds the coord of this scanner relative to the scannerId deonoted in scannerRelativeTo
scannerPositions = [None] * len(scanners)
scannerPositions[0] = [0,0]
scannerRelativeTo = [None] * len(scanners)
scannerRelativeTo[0] = 0

for scannerAId in range(len(scanners)):
  scannerA = scanners[scannerAId]
  for scannerBId in range(len(scanners)):
    if scannerAId == scannerBId: continue
    scannerB = scanners[scannerBId]
    x = 0
    for beacon in scannerA:
      beaconRelatives = []
      for beacon2 in scannerA:
        
