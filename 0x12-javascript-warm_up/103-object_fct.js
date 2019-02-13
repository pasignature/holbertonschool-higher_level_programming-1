#!/usr/bin/node
// Adv problem that does stuff
let myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.incr = function () {
  this.value += 1;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
