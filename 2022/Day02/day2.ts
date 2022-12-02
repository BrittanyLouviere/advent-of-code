import * as fs from 'fs'

let exampleFile :string = "example.txt"
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day02/' + inputFile,'utf8').split("\r\n")

function part1(){
  let totalScore :number = 0
  input.forEach(round => {
    let choices :string[] = round.split(' ')

    // get choices
    let opponent :number = choices[0].charCodeAt(0) - 64
    let me :number = choices[1].charCodeAt(0) - 87

    // get score for choice used
    totalScore += me

    // determine win/lose/tie
    if (opponent == me) { // tie
      totalScore += 3
    } else if ((me == 1 && opponent == 3) || (me == 2 && opponent == 1) || (me == 3 && opponent == 2)) { //win
      totalScore += 6
    }
    // nothing if lose
  });
  return totalScore
}

function part2(){
  let totalScore :number = 0
  input.forEach(round => {
    let choices :string[] = round.split(' ')

    // get choices
    let opponent :number = choices[0].charCodeAt(0) - 64

    // win/lose/tie
    if (choices[1] == "Y") {
      totalScore += 3 // score for tie
      totalScore += opponent // my choice is same as opponent's
    } else if (choices[1] == "Z") {
      totalScore += 6 // score for win
      totalScore += opponent == 3 ? 1 : opponent + 1 // 1 -> 2   2 -> 3   3 -> 1
    } else { 
      //no score for lose (X)
      totalScore += opponent == 1 ? 3 : opponent - 1 // 1 -> 3   2 -> 1    3 -> 2
    }
  });
  return totalScore
}

console.log(part2())