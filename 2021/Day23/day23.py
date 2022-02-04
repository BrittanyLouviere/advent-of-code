#!/usr/bin/python3
import os
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
  for pos in room:
    if pos == ".":
      steps +=1
    elif pos != amphi:
      return None
  return steps

def changeStr (char, index, str):
  return str[:index] + char + str[index+1:]

def canStayInRoom (room, amphi):
  for place in room:
    if place not in [amphi, "."]:
      return False
  return True

def getNewRoomPos (room):
  for pos in reversed(range(len(room))):
    if room[pos] == ".":
      return pos

def findSmallestEnergy(startingState, targetState):
  exploredStates = set()
  states = []
  currState = startingState
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
      newGoalRoom = changeStr(amphi, getNewRoomPos(newRooms[roomNumber]), newRooms[roomNumber])
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
      for pos in range(len(room)):
        if room[pos] != ".":
          amphiPos = pos
          break
      if amphiPos is None: continue
      amphi = room[amphiPos]
      # get hall space just outside room
      hallSpace = goals[chr(roomPos + 65)]
      # check if amphi can immediately go to goal room
      roomNumber = ord(amphi) - 65
      if roomNumber == roomPos and canStayInRoom(currRooms[roomPos], amphi):
        continue # already at goal room and no other types of amphis are there
      steps = findPathToRoom(amphi, currHall, currRooms[roomNumber], hallSpace)
      if steps is not None:
        steps += amphiPos + 1 # add steps to leave room
        newEnergy = currEnergy + (steps * costs[amphi])
        newRooms = list(currRooms)
        newRooms[roomPos] = changeStr(".", amphiPos, room)
        newGoalRoom = changeStr(amphi, getNewRoomPos(newRooms[roomNumber]), newRooms[roomNumber])
        newRooms[roomNumber] = newGoalRoom
        newState = (currHall, tuple(newRooms))
        # if new state not explored yet, add to heapq
        if newState not in exploredStates:
          heapq.heappush(states, (newEnergy, newState))
      # if can't go to goal room, try every available space in hallway
      else:
        for r in [reversed(range(0, hallSpace)), range(hallSpace + 1, 11)]:
          steps = amphiPos + 1 # add steps to leave room
          for newHallSpace in r:
            # if hall space is occupied, break. there will not be a path for the rest
            if currHall[newHallSpace] != ".": break
            steps += 1
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
  return currEnergy

hallway = "." * 11
part1Rooms = []
part2Rooms = []
part2Adds = list(reversed(["DD", "CB", "BA", "AC"]))
with open(input, 'r') as f:
  lines = f.readlines()[2:4]
  for hallSpace in range(3, 10, 2):
    part1Rooms.append((lines[0][hallSpace] + lines[1][hallSpace]))
    part2Rooms.append((lines[0][hallSpace] + part2Adds.pop() + lines[1][hallSpace]))
  part1Rooms = tuple(part1Rooms)
  part2Rooms = tuple(part2Rooms)

part1TargetState = (
  "." * 11,
  ("AA", "BB", "CC", "DD")
)
print("Part 1: ", findSmallestEnergy((hallway, part1Rooms), part1TargetState))

part2TargetState = (
  "." * 11,
  ("A"*4, "B"*4, "C"*4, "D"*4)
)
print("Part 2: ", findSmallestEnergy((hallway, part2Rooms), part2TargetState))