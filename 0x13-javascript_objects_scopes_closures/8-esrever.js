#!/usr/bin/node
// Reverses a list
exports.esrever = function (list) {
  let rev = [];
  for (let i = list.length; i-- > 0;) {
    rev.push(list[i]);
  }
  return rev;
};
