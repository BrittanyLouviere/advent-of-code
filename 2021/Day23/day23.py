#!/usr/bin/python3
import os
from collections import OrderedDict
import heapq

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

costs = {
  "A": 1,
  "B": 10,
  "C": 100,
  "D": 1000
}

goals = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

targetState = (
  "." * 11,
  (("AA"), ("BB"), ("CC"), ("DD"),
  )
)

# returns steps in path to room if valid, otherwise returns None
def findPathToRoom (amphi, hallway, room, hallSpace):
  myGoal = goals[amphi]
  path = None
  if hallSpace < myGoal: 
    path = hallway[hallSpace + 1 : myGoal + 1]
  else: 
    path = hallway[myGoal : hallSpace]
  steps = 0
  #check hallway spaces
  for pathSpace in path:
    if pathSpace != ".":
      return None
    steps += 1
  # check room
  if room[0] != ".":
    return None
  steps += 1
  if room[1] == ".":
    steps += 1
  elif room[1] != amphi: 
    return None
  return steps

def changeStr (char, index, str):
  return str[:index] + char + str[index+1:]

hallway = "." * 11
rooms = []
with open(example, 'r') as f:
  lines = f.readlines()[2:4]
  for hallSpace in range(3, 10, 2):
    rooms.append((lines[0][hallSpace] + lines[1][hallSpace]))
  rooms = tuple(rooms)

exploredStates = set()
states = []
currState = (hallway, rooms)
currEnergy = 0
while currState != targetState:
  # if we explored this state already, skip it
  if currState in exploredStates:
    currEnergy, currState = heapq.heappop(states)
    continue
  # add to list of explored states
  exploredStates.add(currState)
  currHall, currRooms = currState
  # for each amphi in hall, try to enter room
  for hallSpace in range(len(currHall)):
    amphi = currHall[hallSpace]
    # if not an amphipod, skip
    if amphi == ".": continue
    # if no path, skip. else, find total energy cost
    roomNumber = ord(amphi) - 65
    steps = findPathToRoom(amphi, currHall, currRooms[roomNumber], hallSpace)
    if steps is None: continue
    newEnergy = currEnergy + (steps * costs[amphi])
    # find new state
    newHall = changeStr(".", hallSpace, currHall)
    newRooms = list(currRooms)
    newGoalRoom = changeStr(amphi, int(newRooms[roomNumber][1] == "."), newRooms[roomNumber])
    newRooms[roomNumber] = newGoalRoom
    newState = (newHall, tuple(newRooms))
    # if new state not explored yet, add to heapq
    if newState not in exploredStates:
      heapq.heappush(states, (newEnergy, newState))
  # for each amphi in room, try to leave room
  for roomPos in range(len(currRooms)):
    room = currRooms[roomPos]
    # get position of first amphi. if none, skip room
    amphiPos = None
    if room[0] != ".": 
      amphiPos = 0
    elif room[1] != ".": 
      amphiPos = 1
    else: 
      continue
    amphi = room[amphiPos]
    # get hall space just outside room
    hallSpace = goals[chr(roomPos + 65)]
    # check if amphi can immediately go to goal room
    roomNumber = ord(amphi) - 65
    if roomNumber == roomPos and room[1] == amphi:
      continue # is already at goal, skip
    steps = findPathToRoom(amphi, currHall, currRooms[roomNumber], hallSpace)
    if steps is not None:
      steps += amphiPos + 1 # add steps to leave room
      newEnergy = currEnergy + (steps * costs[amphi])
      newRooms = list(currRooms)
      newRooms[roomPos] = changeStr(".", amphiPos, room)
      newGoalRoom = changeStr(amphi, int(newRooms[roomNumber][1] == "."), newRooms[roomNumber])
      newRooms[roomNumber] = newGoalRoom
      newState = (currHall, tuple(newRooms))
      # if new state not explored yet, add to heapq
      if newState not in exploredStates:
        heapq.heappush(states, (newEnergy, newState))
    # if can't go to goal room, try every available space in hallway
    else:
      for r in [reversed(range(0, hallSpace)), range(hallSpace + 1, 11)]:
        steps = amphiPos + 1
        for newHallSpace in r:
          # if hall space is occupied, break. there will not be a path for the rest
          if currHall[newHallSpace] != ".": break
          steps += 1  # add steps to leave room
          # if hall space is in front of room, skip
          if newHallSpace in goals.values(): continue
          newEnergy = currEnergy + (steps * costs[amphi])
          # build new state for new hallway position
          newRooms = list(currRooms)
          newRooms[roomPos] = changeStr(".", amphiPos, room)
          newHall = changeStr(amphi, newHallSpace, currHall)
          newState = (newHall, tuple(newRooms))
          # check if new state has been explored already
          if newState not in exploredStates:
            heapq.heappush(states, (newEnergy, newState))
  currEnergy, currState = heapq.heappop(states)


print("Part 1: ", currEnergy)