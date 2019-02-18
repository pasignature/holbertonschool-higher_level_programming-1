#!/usr/bin/node
// Simple square class
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }
};
