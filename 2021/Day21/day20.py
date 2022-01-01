#!/usr/bin/python3
import os

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

class DeterministicDie:
  number = 0
  rolls = 0
  def __iter__(self):
    return self
  def __next__(self):
    self.number += 1
    self.rolls += 1
    if self.number > 100:
      self.number -= 100
    return self.number

startingPos = [0, 0]
with open(input, 'r') as f:
  startingPos[0] = int(f.readline().strip()[28:])
  startingPos[1] = int(f.readline().strip()[28:])

def part1(startingPos: list()) -> int:
  playerPos = startingPos.copy()
  playerScore = [0, 0]
  turn = False
  die = DeterministicDie()
  while playerScore[0] < 1000 and playerScore[1] < 1000:
    roll = next(die) + next(die) + next(die)
    playerPos[turn] += roll
    while playerPos[turn] > 10:
      playerPos[turn] -= 10
    playerScore[turn] += playerPos[turn]
    turn = not turn
  return die.rolls * playerScore[turn]

def part2(startingPos: list()):
  # all possible rolls per turn
  allRolls = []
  for r1 in range(1, 4):
    for r2 in range(1, 4):
      for r3 in range(1, 4):
        allRolls.append(r1 + r2 + r3)

  # key: (p1Pos, p2Pos, p1Score, p2Score) value: # universes in this state
  universes = {}
  universes[(startingPos[0], startingPos[1], 0, 0)] = 1

  # [p1 wins, p2 wins]
  wins = [0, 0]

  turn = False
  while sum(universes.values()) > 0:
    newUniverses = {}
    for playSet, count in universes.items():
      for roll in allRolls:
        newPlaySet = list(playSet)
        newPlaySet[turn] += roll
        while newPlaySet[turn] > 10:
          newPlaySet[turn] -= 10
        newPlaySet[turn + 2] += newPlaySet[turn]

        if newPlaySet[turn + 2] > 20:
          wins[turn] += count
        else:
          newPlaySet = tuple(newPlaySet)
          x = newUniverses.get(newPlaySet, 0)
          newUniverses[newPlaySet] = x + count
    universes = newUniverses
    turn = not turn
  return max(wins)

print("Part 1: ", part1(startingPos))
print("Part 2: ", part2(startingPos))