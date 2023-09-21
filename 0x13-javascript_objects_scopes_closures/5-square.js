#!/usr/bin/node
/*
 * Square - This is a Class that inherits from the Rectangle class
 * size - is the size of the square
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
