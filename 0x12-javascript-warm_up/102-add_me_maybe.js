#!/usr/bin/node
// A function that incr and calls another function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
