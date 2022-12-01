import * as fs from 'fs';

let examplefile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day01/' + inputFile,'utf8').split("\r\n\r\n");

function part1(){
  let currentMax: number = 0;
  input.forEach(elf => {
    let foodBag = elf.split("\r\n");
    let calories :number = 0;

    foodBag.forEach(food => {
      calories += +food;
    });

    currentMax = calories > currentMax ? calories : currentMax;
  });

  return currentMax;
}

function part2(){
  let calorieCounts: number[] = [];
  input.forEach(elf => {
    let foodBag = elf.split("\r\n");
    let calories :number = 0;

    foodBag.forEach(food => {
      calories += +food;
    });

    calorieCounts.push(calories);
  });

  calorieCounts = calorieCounts.sort((n1,n2) => n2 - n1)
  return calorieCounts[0] + calorieCounts[1] + calorieCounts[2];
}

console.log(part2());