#!/usr/bin/python3
import os
from enum import Enum
from dataclasses import dataclass, field
from math import prod
from typing import List, Tuple

class PacketType(Enum):
  Sum = 0
  Product = 1
  Minimum = 2
  Maximum = 3
  Literal = 4
  GreaterThan = 5
  LessThan = 6
  EqualTo = 7

@dataclass
class Packet:
  version: int
  typeId: PacketType
  value: int = -1
  subPackets: list = field(default_factory=list)

  def getVersionSum(self) -> int:
    subSum = [p.getVersionSum() for p in self.subPackets]
    return self.version + sum(subSum)
  
  def getValue(self) -> int:
    if self.typeId == PacketType.Literal:
      return self.value
    subValues = [p.getValue() for p in self.subPackets]
    if self.typeId == PacketType.Sum:
      return sum(subValues)
    if self.typeId == PacketType.Product:
      return prod(subValues)
    if self.typeId == PacketType.Minimum:
      return min(subValues)
    if self.typeId == PacketType.Maximum:
      return max(subValues)
    if self.typeId == PacketType.GreaterThan:
      return int(subValues[0] > subValues[1])
    if self.typeId == PacketType.LessThan:
      return int(subValues[0] < subValues[1])
    if self.typeId == PacketType.EqualTo:
      return int(subValues[0] == subValues[1])

# return (parsed #, bits read)
def parseLiteral(bits: str) -> Tuple[int, int]:
  bitIndex = 0
  firstBit = "1"
  currentByte = ""
  biNum = ""
  while firstBit == "1":
    firstBit = bits[bitIndex]
    currentByte = bits[bitIndex+1:bitIndex+5]
    bitIndex += 5
    biNum += currentByte
  return (int(biNum, 2), bitIndex)

# return (sub packets list, bits read)
def parseOperator(bits: str) -> Tuple[List[Packet], int]:
  bitIndex = 0
  lengthType = bits[bitIndex]
  bitIndex += 1
  subPackets = []
  if lengthType == '0': # total length in bits
    length = int(bits[bitIndex:bitIndex+15], 2)
    bitIndex += 15
    goal = length + bitIndex
    while bitIndex < goal:
      subBinary = bits[bitIndex:bitIndex+length]
      packet, bitAdd = parsePacket(subBinary)
      subPackets.append(packet)
      bitIndex += bitAdd
  else: # number of sub packets
    length = int(bits[bitIndex:bitIndex+11], 2)
    bitIndex += 11
    for i in range(length):
      subBinary = bits[bitIndex:]
      packet, bitAdd = parsePacket(subBinary)
      subPackets.append(packet)
      bitIndex += bitAdd
  return (subPackets, bitIndex)

# return (Packet object, bits read)
def parsePacket(bits: str) -> Tuple[Packet, int]:
  version = int(bits[0:3], 2)
  typeID = PacketType(int(bits[3:6], 2))
  bitIndex = 6

  if typeID == PacketType.Literal: # literal packet
    contents, addIndex = parseLiteral(bits[bitIndex:])
    bitIndex += addIndex
    return (Packet(version, typeID, contents), bitIndex)
  else: # operator packet
    subPackets, bitAdd = parseOperator(bits[bitIndex:])
    bitIndex += bitAdd
    return (Packet(version, typeID, subPackets=subPackets), bitIndex)

root = os.path.dirname(os.path.abspath(__file__))
example = os.path.join(root, 'Example.txt')
input = os.path.join(root, 'Input.txt')
bigboy = os.path.join(root, 'BigBoy.txt')

hexMessage = ""
with open(input, 'r') as f:
  hexMessage = f.readline().strip()

biMessage = ""
for char in hexMessage:
  binary = "{0:0>4b}".format(int(char, 16))
  biMessage += binary

topPacket, _ = parsePacket(biMessage)

print("Part 1: ", topPacket.getVersionSum())
print("Part 1: ", topPacket.getValue())