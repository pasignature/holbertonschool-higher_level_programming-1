#!/usr/bin/node
// imports and array and computes a new array
let data = require('./100-data').list;
console.log(data);
console.log(data.map((x, index) => x * index));
