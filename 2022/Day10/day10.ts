import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day10/' + inputFile,'utf8').split("\r\n");

function part1(){
  let register :number = 1
  let cycle :number = 1     // cycles STARTED
  let instIndex :number = 0
  let value :number|undefined = undefined
  let signalSum :number = 0
  while (instIndex < input.length) {
    if (value != undefined){
      register += value
      value = undefined
      instIndex++
    }
    else if(input[instIndex] == "noop") {
      instIndex++
    }
    else {
      value = +input[instIndex].replace("addx ", "")
    }
    cycle++
    if ((cycle - 20) % 40 == 0) {
      //console.log("cycle:" + cycle + " register:" + register + " signal:" + cycle*register)
      signalSum += cycle * register
    }
  }
  return signalSum
}

function part2(){
  let register :number = 1
  let cycle :number = 1     // cycles STARTED
  let instIndex :number = 0
  let value :number|undefined = undefined
  let crtLocation : number = 0
  let image :string[] = [""]
  while (instIndex < input.length) {
    // draw pixel
    if ([register, register+1, register-1].includes(image[image.length-1].length)) {
      image[image.length-1] += "#"
    }
    else {
      image[image.length-1] += " "
    }

    if (image[image.length-1].length == 40 ) {
      image.push("")
    }

    // execute instructions
    if (value != undefined){
      register += value
      value = undefined
      instIndex++
    }
    else if(input[instIndex] == "noop") {
      instIndex++
    }
    else {
      value = +input[instIndex].replace("addx ", "")
    }
    cycle++
  }
  return image.join("\n")
}

console.log(part2());