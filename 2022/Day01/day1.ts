import * as fs from 'fs';

let examplefile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day01/' + inputFile,'utf8').split("\r\n\r\n");

let currentMax: number = 0;
input.forEach(elf => {
  let foodBag = elf.split("\r\n");
  let calories :number = 0;

  foodBag.forEach(food => {
    calories += +food;
  });

  currentMax = calories > currentMax ? calories : currentMax;
});

console.log(currentMax);