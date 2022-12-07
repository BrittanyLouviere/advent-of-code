import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day07/' + inputFile,'utf8').split("\r\n");

function getDirSizes(){
  let dirSizes :Map<string, number> = new Map()
  dirSizes.set("/", 0)
  let activeDirs :string[] = []
  let checkedFiles :string[] = []

  input.forEach(line => {
    if (line.startsWith("$")) { // handle a command
      if (line == "$ cd /")
        activeDirs = ["/"]
      else if (line == "$ cd ..")
        activeDirs.pop()
      else if (line.startsWith("$ cd")) {
        let dir :string = activeDirs.join("/") + "/" + line.replace("$ cd ", "")  // some dirs in different places have the same name...
        activeDirs.push(dir)
        if (!dirSizes.has(dir))
          dirSizes.set(dir, 0) // do we visit the same dir multiple times???? YUP
      }
    }
    else if (!line.startsWith("dir ")){ // handle a listed file
      let splitFile :string[] = line.split(" ") // 0:size 1:name
      let filePath :string = activeDirs.join("/") + "/" + splitFile[1]
      if (!checkedFiles.includes(filePath)) {
        let fileSize :number = +splitFile[0]
        activeDirs.forEach(dir => {
          dirSizes.set(dir, dirSizes.get(dir)! + fileSize)
        });
        checkedFiles.push(filePath)
      }
    }
  });

  return dirSizes
}

function part1(){
  let dirSizes :Map<string, number> = getDirSizes()
  return Array.from(dirSizes.values()).filter(x => x <= 100000).reduce((a,b)=>a+b)
}

function part2(){
  let dirSizes :Map<string, number> = getDirSizes()
  let leftToFree :number = 30000000 - (70000000 - dirSizes.get("/")!)
  let smallestDir :number

  Array.from(dirSizes.values()).forEach(dirSize => {
    if (dirSize >= leftToFree && (smallestDir == undefined || smallestDir > dirSize)) {
      smallestDir = dirSize
    }
  });

  return smallestDir!
}

console.log(part2());