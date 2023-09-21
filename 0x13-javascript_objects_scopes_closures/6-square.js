#!/usr/bin/node

const PSquare = require('./5-square');

class Square extends PSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === 'C') {
      for (let i = 0; i < 4; i++) {
        let row = '';
        for (let j = 0; j < 4; j++) {
          row += 'C';
        }
        console.log(row);
      }
    } else {
      for (let i = 0; i < 4; i++) {
        let row = '';
        for (let j = 0; j < 4; j++) {
          row += 'X';
        }
        console.log(row);
      }
    }
  }
}
module.exports = Square;
