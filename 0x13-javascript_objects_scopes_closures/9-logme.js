#!/usr/bin/node
// displays number of args
let numArgs = 0;
exports.logMe = function (item) {
  console.log(numArgs + ': ' + item);
  numArgs++;
};
