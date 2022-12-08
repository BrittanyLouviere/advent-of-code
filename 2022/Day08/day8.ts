import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input :number[][] = fs.readFileSync('Day08/' + inputFile,'utf8').split("\r\n").map(x => x.split("").map(x => +x));

function part1(){
  let visibleCount :number = 0
  for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input[i].length; j++) {
      const tree :number = input[i][j];
      let column :number[] = input.map(function(value,index) { return value[j]; })
      let left  :number = Math.max(...input[i].slice(0, j))
      let right :number = Math.max(...input[i].slice(j+1))
      let above :number = Math.max(...column.slice(0, i))
      let below :number = Math.max(...column.slice(i+1))

      if (tree > left || tree > right || tree > above || tree > below)
        visibleCount++
    }
  }
  return visibleCount
}

function part2(){
  let highestScore :number = 0
  for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input[i].length; j++) {
      const tree :number = input[i][j];
      let column :number[] = input.map(function(value,index) { return value[j]; })
      let directions  :number[][] = [
        input[i].slice(0, j).reverse(), // left
        input[i].slice(j+1),            // right
        column.slice(0, i).reverse(),   // above
        column.slice(i+1)               // below
    ]

      let treeScore :number = 1
      for (let index = 0; index < directions.length; index++) {
        let dirScore :number = 0
        directions[index].every(element => {
          dirScore++
          if (element >= tree)
            return false
          return true
        });
        treeScore *= dirScore
      }

      highestScore = Math.max(treeScore, highestScore)
    }
  }
  return highestScore
}

console.log(part2());