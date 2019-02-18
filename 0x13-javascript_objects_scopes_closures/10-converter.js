#!/usr/bin/node
// Converts a number from base10 to another
exports.converter = function (base) {
  return function changeBase (val) {
    return val.toString(base);
  }
};
