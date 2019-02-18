#!/usr/bin/node
// Simple square class
module.exports = class Square extends require('./4-rectangle') {
  constructor (size) {
    super(size, size);
  }
  charPrint (c = 'X') {
    for (let y = 0; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }
};
