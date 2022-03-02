#!/usr/bin/node
// class Square that defines a square and inherits from Square of 5-square.js
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.height; x++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
