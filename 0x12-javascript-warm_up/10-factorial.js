#!/usr/bin/node
// This script that computes and prints a factorial.
function factorial (myVar) {
  if (isNaN(myVar)) {
    return (1);
  } else if (myVar === 0) {
    return (1);
  } else {
    return (myVar * factorial(myVar - 1));
  }
}

const MyVar = parseInt(process.argv[2]);
if (MyVar > 0); {
  const result = factorial(MyVar);
  console.log(result);
}
