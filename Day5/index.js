const rawProcedureData = require("fs").readFileSync('./input.txt', 'utf-8').split('\n')
const startingPositions = require("fs").readFileSync('./startingPositions.txt', 'utf-8')

let startingStack = startingPositions.split('\n');
// Pop the index numbers
startingStack.pop()
// Reverse to work with the bottom first.
startingStack.reverse()
let stackCount = 9
let stacks = []
let procedure = rawProcedureData.map(row => {
  let rowComponents = row.split(' ')
  return [Number(rowComponents[1]), Number(rowComponents[3]), Number(rowComponents[5])]
})

// Initialize stack
for (let i = 0; i < stackCount; i++) {
  stacks[i] = []
}

// Set up starting stack
startingStack.map((row, rowNumber) => {
  rowValues = row.match(/[A-Z]|( ?    ?)/g);

  rowValues.map((crate, stackNumber) => {
    let crateValue = crate.trim();
    if (crateValue) {
      // console.log(`Crate ${crateValue}, Row ${rowNumber}, Stack ${stackNumber}`);
      stacks[stackNumber][rowNumber] = crateValue;
    }
  })
})

function moveCrate(startingStackNumber, endingStackNumber) {
  let crateToBeMoved = stacks[startingStackNumber].pop()
  stacks[endingStackNumber].push(crateToBeMoved)
}

function moveManyCrates(numOfCratesToMove, startingStackNumber, endingStackNumber) {
  for (let i = 0; i < numOfCratesToMove; i++) {
    moveCrate(startingStackNumber, endingStackNumber);
  }
}

procedure.forEach(operation => {
  moveManyCrates(operation[0], operation[1] - 1, operation[2] - 1)
})

console.log('Final stack arrangement');
console.table(stacks)
console.log('Crates on top', stacks.map(stack => stack[stack.length - 1]).join(''));
