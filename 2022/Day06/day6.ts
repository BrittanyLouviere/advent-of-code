import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day06/' + inputFile,'utf8').split("");

function part1(){
  let characterCount :number = 0
  let charMap :Map<string, number> = new Map

  for (let index = 0; index < input.length; index++) {
    const character = input[index];
    characterCount++      // increment count
    if (!charMap.has(character))
      charMap.set(character, 0)

    charMap.set(character, charMap.get(character)! + 1) // add new character
    if (index > 3) {      // remove old character and check for repeats
      let oldChar :string = input[index-4]
      charMap.set(oldChar, charMap.get(oldChar)! -1)

      if (charMap.get(oldChar)! == 0) 
        charMap.delete(oldChar)

      if (Array.from(charMap.values()).filter(x => x > 1).length == 0) 
        return characterCount
    }
  }
}

function part2(){
  let characterCount :number = 0
  let charMap :Map<string, number> = new Map

  for (let index = 0; index < input.length; index++) {
    const character = input[index];
    characterCount++      // increment count
    if (!charMap.has(character))
      charMap.set(character, 0)

    charMap.set(character, charMap.get(character)! + 1) // add new character
    if (index > 13) {      // remove old character and check for repeats
      let oldChar :string = input[index-14]
      charMap.set(oldChar, charMap.get(oldChar)! -1)

      if (charMap.get(oldChar)! == 0) 
        charMap.delete(oldChar)

      if (Array.from(charMap.values()).filter(x => x > 1).length == 0) 
        return characterCount
    }
  }
}

console.log(part2());