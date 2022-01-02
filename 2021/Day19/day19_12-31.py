#!/usr/bin/python3
import os
from queue import SimpleQueue
from math import copysign
import queue

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
example2 = os.path.join(root, 'Example2.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

scanners = []
with open(input, 'r') as f:
  for line in f.readlines():
    if "---" in line:
      scanners.append([])
    elif str.isspace(line):
      continue
    else:
      scanners[-1].append(list(map(int, line.strip().split(","))))

# beacons relative to each other per scanner
# axes: 
#   1 = scanner
#   2 = beacon that coords are relative too
#   3 = coordinates of other beacons within scanner relative to this beacon
#   4 = x, y, and z coordinates
relativeBeacons = SimpleQueue()
for scanner in scanners:
  temp = []
  for beaconA in scanner:
    temp.append([])
    for beaconB in scanner:
      temp[-1].append([])
      for i in range(3):
        temp[-1][-1].append(beaconA[i] - beaconB[i])
  relativeBeacons.put(temp)

def coordsMatch(locationA, locationB):
  coordsA = list(map(abs, locationA))
  coordsB = list(map(abs, locationB))
  positions = []
  signs = []
  for coord in coordsB:
    if coord not in coordsA: return None #not a match
    indexA = coordsA.index(coord)
    indexB = coordsB.index(coord)
    signA = int(copysign(1, locationA[indexA]))
    signB = int(copysign(1, locationB[indexB]))
    signs.append(signA * signB)
    positions.append(int(indexA))
  return (tuple(positions), tuple(signs)) #is a match

def findMatch(foundBeacons, newBeacons):
  for foundBeacon in reversed(foundBeacons):
    for newBeacon in newBeacons:
      matches = {}
      for newLocation in newBeacon:
        for foundLocation in foundBeacon:
          result = coordsMatch(foundLocation, newLocation)
          if result is not None:
            if result not in matches.keys():
              matches[result] = [None] * len(foundBeacon)
            if newLocation == [0,0,0]:
              for match in matches.values():
                match[foundBeacon.index(foundLocation)] = newBeacon.index(newLocation)
            else:
              matches[result][foundBeacon.index(foundLocation)] = newBeacon.index(newLocation)
            continue

      for key, val in matches.items():
        count = len(foundBeacon) - val[:len(foundBeacon)].count(None)
        if count > 10: 
          return (key, val)
  return None

def addNewBeacons(positions, signs, foundIndexs, newBeacons, templateBeacon):
  # get list of new beacons
  beaconsToAdd = []
  for index in range(len(newBeacons)):
    if index not in foundIndexs:
      beaconsToAdd.append(newBeacons[index])
  
  # fix coordinate signs and order
  orientedBeacons = []
  for beacon in beaconsToAdd:
    orientedBeacons.append([])
    for location in beacon:
      newLocation = [0,0,0]
      for oldIndex in range(3):
        oldNumber = location[oldIndex]
        newIndex = positions[oldIndex]
        sign = signs[oldIndex]
        newLocation[newIndex] = oldNumber * sign
      orientedBeacons[-1].append(newLocation)

  # fix order of relative coordinates
  fixedBeacons = []
  conversions = []
  for beacon in orientedBeacons:
    temp = [None] * len(foundIndexs)
    conversion = []
    for oldIndex in range(len(beacon)):
      oldVal = beacon[oldIndex]
      try: newIndex = foundIndexs.index(oldIndex)
      except: newIndex = None
      if newIndex == None:
        temp.append(oldVal)
      else:
        temp[newIndex] = oldVal
        if len(conversion) == 0:
          for coord in range(3):
            conversion.append(oldVal[coord] - templateBeacon[newIndex][coord])
    fixedBeacons.append(temp)
    conversions.append(conversion)

  # add in missing coordinates
  for index in range(len(fixedBeacons)):
    beacon = fixedBeacons[index]
    conversion = conversions[index]
    for locInd in range(len(beacon)):
      if beacon[locInd] is not None: continue
      tempLoc = templateBeacon[locInd]
      newLoc = []
      for i in range(3):
        newLoc.append(tempLoc[i] + conversion[i])
      beacon[locInd] = newLoc

  return fixedBeacons

queueLength = 24
checkedWOFound = 0
beaocnsFound = 1

foundBeacons:list = relativeBeacons.get()
while not relativeBeacons.empty():
  newBeacons = relativeBeacons.get()
  result = findMatch(foundBeacons, newBeacons)
  if result is None:
    relativeBeacons.put(newBeacons)
    checkedWOFound += 1
  else:
    beaocnsFound += 1
    print("found {}!".format(beaocnsFound))
    orientedBeacons = addNewBeacons(result[0][0], result[0][1], result[1], newBeacons, foundBeacons[0])
    # add new beacon locations to existing ones
    for beaconInd in range(len(foundBeacons)):
      beacon: list = foundBeacons[beaconInd]
      for newBeaconInd in  range(len(orientedBeacons)):
        #beacon.append(orientedBeacons[newBeaconInd][beaconInd])
        beacon.append([])
        for coord in orientedBeacons[newBeaconInd][beaconInd]:
          beacon[-1].append(coord * -1)

    # add new beacons
    foundBeacons.extend(orientedBeacons)
    checkedWOFound = 0
    queueLength -= 1

print("Part 1: ", len(foundBeacons))