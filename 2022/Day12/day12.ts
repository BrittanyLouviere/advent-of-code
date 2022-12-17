import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day12/' + inputFile,'utf8').split("\r\n");

function part1(){
  let map :number[][] = []
  let start :[number, number] = [-1, -1]
  let end :[number, number] = [-1, -1]
  
  // get map, start, and end
  input.forEach(line => {
    map.push(line.split("").map(x => x.charCodeAt(0)-97))
    if (line.includes("S")) {
      start = [map.length-1, line.indexOf("S")]
      map[start[0]][start[1]] = 0
    }
    if (line.includes("E")) {
      end = [map.length-1, line.indexOf("E")]
      map[end[0]][end[1]] = 25
    }
  });

  let path :Map<string, string> = new Map()
  let steps :Map<string, number> = new Map()
  let current :number[] = start
  let toVisit :number[][] = []

  steps.set(`${current[0]},${current[1]}`, 0)

  // traverse map 
  while (current != undefined
        && (current[0] != end[0] || current[1] != end[1])){
    let udlr = [
      [current[0]-1, current[1]], // up
      [current[0]+1, current[1]], // down
      [current[0], current[1]-1], // left
      [current[0], current[1]+1]  // right
    ]
    let currentElevation :number = map[current[0]][current[1]]
    let currString :string = `${current[0]},${current[1]}`

    udlr.forEach(direction => {
      let direString :string = `${direction[0]},${direction[1]}`
      if (direction[0] > -1 
        && direction[1] > -1 
        && direction[0] < map.length
        && direction[1] < map[0].length
        && (!path.has(`${direction[0]},${direction[1]}`) || steps.get(direString)! > steps.get(currString)!+1)
        && map[direction[0]][direction[1]] - currentElevation < 2
        ) {
          path.set(direString, currString)
          toVisit.push(direction)
          steps.set(direString, steps.get(currString)! + 1)
      }
    });
    current = toVisit.shift()!
  }
  return steps.get(`${current[0]},${current[1]}`)
}

function part2(){
  let map :number[][] = []
  let end :[number, number] = [-1, -1]
  let toVisit :number[][] = []
  let steps :Map<string, number> = new Map()
  let path :Map<string, string> = new Map()
  
  // get map, and end
  input.forEach(line => {
    map.push(line.split("").map(x => x.charCodeAt(0)-97))
    if (line.includes("S")) {
      map[map.length-1][line.indexOf("S")] = 0
    }
    if (line.includes("E")) {
      end = [map.length-1, line.indexOf("E")]
      map[end[0]][end[1]] = 25
    }

    for (let index = 0; index < line.length; index++) {
      const element = map[map.length-1][index];
      if (element == 0) {
        toVisit.push([map.length-1, index])
        steps.set(`${map.length-1},${index}`, 0)
        path.set(`${map.length-1},${index}`, "")
      }
    }
  });

  let current :number[] = toVisit.shift()!

  // traverse map 
  while (current != undefined){
    let udlr = [
      [current[0]-1, current[1]], // up
      [current[0]+1, current[1]], // down
      [current[0], current[1]-1], // left
      [current[0], current[1]+1]  // right
    ]
    let currentElevation :number = map[current[0]][current[1]]
    let currString :string = `${current[0]},${current[1]}`

    udlr.forEach(direction => {
      let direString :string = `${direction[0]},${direction[1]}`
      if (direction[0] > -1 
        && direction[1] > -1 
        && direction[0] < map.length
        && direction[1] < map[0].length
        && (!path.has(`${direction[0]},${direction[1]}`) || steps.get(direString)! > steps.get(currString)!+1)
        && map[direction[0]][direction[1]] - currentElevation < 2
        ) {
          path.set(direString, currString)
          toVisit.push(direction)
          steps.set(direString, steps.get(currString)! + 1)
      }
    });
    current = toVisit.shift()!
  }
  return steps.get(`${end[0]},${end[1]}`)
}

console.log(part2());