#!/usr/bin/python3
import os

drawnNums = []
file = None
def getInput(input):
  global file 
  global drawnNums
  file = open(input, 'r')
  drawnNums = [int(x) for x in file.readline().strip().split(',')]

def solution():
  cardSize = -1
  board = []
  winner = None
  loser = None
  while (line := file.readline()):
    if line.isspace(): continue #skip blank lines
    for num in line.strip().split(): #add numbers to board
      board.append(int(num))
    if (cardSize == -1): cardSize = len(board)

    if len(board) == cardSize * cardSize: #calculate board stuff
      col = [0] * cardSize
      row = [0] * cardSize
      for num in drawnNums:
        try:
          index = board.index(num)
          col[index % cardSize] += 1
          row[index // cardSize] += 1
          board[index] = -1
          if(col.count(cardSize) > 0 or row.count(cardSize) > 0):
            winIndex = drawnNums.index(num)
            countCalled = board.count(-1)
            if (winner == None or winIndex < winner[0]):
              winner = (winIndex, sum(board) + countCalled)
            if (loser == None or winIndex > loser[0]):
              loser = (winIndex, sum(board) + countCalled)
            break
        except ValueError:
          pass
      board.clear()

  winningNum = drawnNums[winner[0]]
  boardSum = winner[1]
  print("winner: ", boardSum, " * ", winningNum, " = ", winningNum * boardSum)
  winningNum = drawnNums[loser[0]]
  boardSum = loser[1]
  print("loser: ", boardSum, " * ", winningNum, " = ", winningNum * boardSum)

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

getInput(input)
solution()