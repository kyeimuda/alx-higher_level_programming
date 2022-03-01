#!/usr/bin/node
// This script searches the second biggest integer in the list of arguments.
function largest2 (arr, size) {
  if (size <= 3) {
    console.log(0);
  } else {
    arr.splice(0, 2);
    arr.sort(function (a, b) { return b - a; });
    console.log(parseInt(arr[1]));
  }
}
const myVar = process.argv;
const myVarSize = process.argv.length;
largest2(myVar, myVarSize);
