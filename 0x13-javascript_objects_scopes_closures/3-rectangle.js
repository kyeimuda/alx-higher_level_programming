#!/usr/bin/node
// Create an instance method called print() that prints the rectangle using the character X
class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let x = 0; x < this.height; x++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle
