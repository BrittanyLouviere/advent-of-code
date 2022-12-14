import * as fs from 'fs';

let exampleFile :string = "example.txt";
let inputFile :string = "input.txt"
const input = fs.readFileSync('Day11/' + inputFile,'utf8').split("\r\n\r\n");

function part1(){
  // parse monkeys
  let items :number[][] = []
  //               opp     opp #   % by    false   true
  let operations :[string, string, number, number, number][] = []
  let inspectionCount :number[] = []
  input.forEach(piece => {
    let monkey :string[] = piece.split("\r\n")
    items.push(monkey[1].replace("  Starting items: ", "").split(", ").map(x => +x))
    operations.push([
      monkey[2].split(" ")[6],
      monkey[2].split(" ")[7],
      +monkey[3].split(" ")[5],
      +monkey[5].split(" ")[9],
      +monkey[4].split(" ")[9]
    ])
    inspectionCount.push(0)
  });

  // engage in monkey business
  //console.log(items)
  //console.log(operations)
  for (let round = 0; round < 20; round++) {
    for (let monkeyIndex = 0; monkeyIndex < items.length; monkeyIndex++) {
      let currentItems :number[] = items[monkeyIndex];
      const ops :[string, string, number, number, number] = operations[monkeyIndex]
      
      while (items[monkeyIndex].length > 0) {
        // monkey inspects item: run operation
        inspectionCount[monkeyIndex]++
        let item = currentItems[0];
        let inspectionValue = ops[1] == "old" ? item : +ops[1]
        if (ops[0] == "*")
          item *= inspectionValue
        else if (ops[0] == "+")
          item += inspectionValue

        // worry level is divided by 3 (round down)
        item = Math.floor(item / 3)

        // monkey tests worry level: use % test
        //    and throws to chosen monkey
        //console.log(`item:${item}\ncheck:${(item % ops[2] == 0)}\nopsIndex:${3 + +(item % ops[2] == 0)}\nmonkey:ops[3 + +(item % ops[2] == 0)]`)
        let chosenMonkey :number = +ops[3 + +(item % ops[2] == 0)]
        items[monkeyIndex].shift()
        items[chosenMonkey].push(item)
        //console.log(`Monkey ${monkeyIndex} throws item ${item} to monkey ${chosenMonkey}`)
        //console.log(items)
      }
    }
    //console.log(items)
  }
  //console.log(items)
  inspectionCount.sort((x :number, y :number) => {return y - x})
  //console.log(inspectionCount)
  return inspectionCount[0] * inspectionCount[1]
}

function part2(){
  // parse monkeys
  let items :bigint[][] = []
  //               opp     opp #   % by    false   true
  let operations :[string, string, number, number, number][] = []
  let inspectionCount :number[] = []
  let modulos :number = 1
  input.forEach(piece => {
    let monkey :string[] = piece.split("\r\n")
    items.push(monkey[1].replace("  Starting items: ", "").split(", ").map(x => BigInt(x)))
    operations.push([
      monkey[2].split(" ")[6],
      monkey[2].split(" ")[7],
      +monkey[3].split(" ")[5],
      +monkey[5].split(" ")[9],
      +monkey[4].split(" ")[9]
    ])
    modulos *= +monkey[3].split(" ")[5]
    inspectionCount.push(0)
  });

  for (let round = 0; round < 10000; round++) {
    let count = 0
    for (let monkeyIndex = 0; monkeyIndex < items.length; monkeyIndex++) {
      let currentItems :bigint[] = items[monkeyIndex];
      const ops :[string, string, number, number, number] = operations[monkeyIndex]
      
      while (items[monkeyIndex].length > 0) {
        count++

        // monkey inspects item: run operation
        inspectionCount[monkeyIndex]++
        let item :bigint = currentItems[0];
        let inspectionValue :bigint = ops[1] == "old" ? item : BigInt(ops[1])
        if (ops[0] == "*")
          item = BigInt(item * inspectionValue)
        else if (ops[0] == "+")
          item = item + inspectionValue

        // reduce worry level
        item = item % BigInt(modulos)

        // monkey tests worry level: use % test
        //    and throws to chosen monkey
        let chosenMonkey :number = +ops[3 + +(Number(item) % ops[2] == 0)]
        items[monkeyIndex].shift()
        items[chosenMonkey].push(item)
      }
    }
  }
  inspectionCount.sort((x :number, y :number) => {return y - x})
  return inspectionCount[0] * inspectionCount[1]
}

console.log(part2());