import * as fs from 'fs';

let exampleFile :string = "example.txt";
let exampleFile2 :string = "example2.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day09/' + inputFile,'utf8').split("\r\n");

function part1(){
  let head :[number, number] = [0, 0]
  let tail :[number, number] = [0, 0]
  let visited :Set<string> = new Set()
  visited.add("0,0")

  input.forEach(element => {
    let directions :string[] = element.split(" ")
    let direction :string = directions[0]
    let amount :number = +directions[1]

    for (let index = 0; index < amount; index++) {
      if (direction == "U")
        head[1]++
      else if (direction == "D")
        head[1]--
      else if (direction == "R")
        head[0]++
      else if (direction == "L")
        head[0]--

      
      
      let diff :number[] = head.map((value, index) => value - tail[index])
      if (diff[0] == 2) {
        tail[0]++
        tail[1] += diff[1]
      }  
      else if (diff[0] == -2) {
        tail[0]--
        tail[1] += diff[1]
      }  
      else if (diff[1] == 2) {
        tail[1]++
        tail[0] += diff[0]
      }
      else if (diff[1] == -2) {
        tail[1]--
        tail[0] += diff[0]
      }
      visited.add(tail.join(","))
    }
  });
  return visited.size
}

function part2(){
  let rope :[number, number][] = []
  let knotCount = 10
  for (let index = 0; index < knotCount; index++) {
    rope.push([0, 0])
  }

  let visited :Set<string> = new Set()
  visited.add("0,0")

  input.forEach(element => {
    let directions :string[] = element.split(" ")
    let direction :string = directions[0]
    let amount :number = +directions[1]
    for (let index = 0; index < amount; index++) {
      if (direction == "U")
        rope[0][1]++
      else if (direction == "D")
        rope[0][1]--
      else if (direction == "R")
        rope[0][0]++
      else if (direction == "L")
        rope[0][0]--

      for (let index = 0; index < rope.length-1; index++) {
        const prevKnot :[number, number] = rope[index];
        let currentKnot :[number, number] = rope[index + 1];
        let diff :number[] = prevKnot.map((value, index) => value - currentKnot[index])
        
        if (diff.every(x => Math.abs(x) != 2))        // do nothing
          continue
        else if (diff.every(x => Math.abs(x) != 0)) {  // move both
          currentKnot[0] += Math.abs(diff[0]) == 1 ? diff[0] : diff[0] > 0 ? diff[0]-1 : diff[0]+1
          currentKnot[1] += Math.abs(diff[1]) == 1 ? diff[1] : diff[1] > 0 ? diff[1]-1 : diff[1]+1
        }
        else if (diff.every(x => Math.abs(x) != 1)) {  // move 1
          currentKnot[0] += diff[0] == 0 ? 0 : diff[0] > 0 ? diff[0]-1 : diff[0]+1
          currentKnot[1] += diff[1] == 0 ? 0 : diff[1] > 0 ? diff[1]-1 : diff[1]+1
        }
      }
      visited.add(rope[rope.length-1].join(","))
    }
  });
  return visited.size
}

console.log(part2());