import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day04/' + inputFile,'utf8').split("\r\n");

function part1(){
  let containedCount :number = 0
  input.forEach(pair => {
    let sections :number[] = pair.split(/[-,]+/).map(Number)
    containedCount += +((sections[0] >= sections[2] && sections[1] <= sections[3]) ||
                        (sections[2] >= sections[0] && sections[3] <= sections[1]))
  });
  return containedCount
}

function part2(){
  let containedCount :number = 0
  input.forEach(pair => {
    let sections :number[] = pair.split(/[-,]+/).map(Number)
    containedCount += +((sections[2] >= sections[0] && sections[2] <= sections[1]) ||
                        (sections[0] >= sections[2] && sections[0] <= sections[3]))
  });
  return containedCount
}

console.log(part2());