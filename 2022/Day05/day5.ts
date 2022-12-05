import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day05/' + inputFile,'utf8').split("\r\n\r\n");

function part1(){
  // parse stack
  let layers :string[] = input[0].split("\r\n")
  layers.pop()
  let stacks :string[][] = []

  layers.reverse().forEach(layer => {
    let fixedLayer :string = layer.replace(/    /g, "-").replace(/[ \[\]]/g, "")
    if (stacks.length == 0) {
      stacks = Array.apply(null, Array(fixedLayer.length)).map(function (x, i) { return new Array(); })
    }

    for (let index = 0; index < fixedLayer.length; index++) {
      const crate = fixedLayer[index];
      if (crate != "-") {
        stacks[index].push(crate)
      }
    }
  });

  // parse instructions
  input[1].split("\r\n").forEach(instruction => {
    let inst :string[] = instruction.split(" ")
    const fromStack :number = +inst[3] - 1
    const toStack :number = +inst[5] - 1
    for (let index = 0; index < +inst[1]; index++) {
      stacks[toStack].push(stacks[fromStack].pop()!)
    }
  });

  // get top box for each stack
  let answer :string = ""
  stacks.forEach(stack => {
    answer += stack[stack.length-1]
  });

  return answer
}

function part2(){
  // parse stack
  let layers :string[] = input[0].split("\r\n")
  layers.pop()
  let stacks :string[][] = []

  layers.reverse().forEach(layer => {
    let fixedLayer :string = layer.replace(/    /g, "-").replace(/[ \[\]]/g, "")
    if (stacks.length == 0) {
      stacks = Array.apply(null, Array(fixedLayer.length)).map(function (x, i) { return new Array(); })
    }

    for (let index = 0; index < fixedLayer.length; index++) {
      const crate = fixedLayer[index];
      if (crate != "-") {
        stacks[index].push(crate)
      }
    }
  });

  // parse instructions
  input[1].split("\r\n").forEach(instruction => {
    let inst :string[] = instruction.split(" ")
    const fromStack :number = +inst[3] - 1
    const toStack :number = +inst[5] - 1
    let crane :string[] = new Array()

    for (let index = 0; index < +inst[1]; index++) {
      crane.push(stacks[fromStack].pop()!)
    }
    
    while (crane.length > 0) {
      stacks[toStack].push(crane.pop()!)
    }
  });

  // get top box for each stack
  let answer :string = ""
  stacks.forEach(stack => {
    answer += stack[stack.length-1]
  });

  return answer
}

console.log(part2());