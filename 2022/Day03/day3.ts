import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day03/' + inputFile,'utf8').split("\r\n");

function part1(){
  let itemTotal :number = 0

  input.forEach(bag => {
    // separate compartments
    let compartment1 :string[] = [...new Set(bag.substring(0, bag.length / 2).split(""))]
    let compartment2 :string[] = [...new Set(bag.substring(bag.length / 2).split(""))]

    // find the shared item
    let sharedItem : number = -1
    compartment1.every(item => {
      if (compartment2.includes(item)) {
        sharedItem = item.charCodeAt(0)
        return false
      }
      return true
    });

    // calculate shared item's value and add to total
    itemTotal += sharedItem > 96 ? sharedItem - 96 : sharedItem - 38
  });

  return itemTotal
}

function part2(){
  let itemTotal :number = 0
  for (let index = 0; index < input.length; index += 3) {
    const elf1 = [...new Set(input[index])]
    const elf2 = [...new Set(input[index+1])]
    const elf3 = [...new Set(input[index+2])]

    let sharedItem :number = -1
    elf1.every(item => {
      if (elf2.includes(item) && elf3.includes(item)){
        sharedItem = item.charCodeAt(0)
        return false
      }
      return true
    })

    itemTotal += sharedItem > 96 ? sharedItem - 96 : sharedItem - 38
  }

  return itemTotal
}

console.log(part2());