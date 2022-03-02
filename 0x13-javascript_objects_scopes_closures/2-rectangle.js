#!/usr/bin/node
// a class Rectangle that defines a rectangle:
class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
