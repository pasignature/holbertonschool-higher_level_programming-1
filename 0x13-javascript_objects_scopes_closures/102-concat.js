#!/usr/bin/node
// Concats 2 files and outputs to another file
let fs = require('fs');
fs.readFile(process.argv[2], function (err, data) {
  if (err) {
    return;
  }
  fs.appendFile(process.argv[4], data, {});
});
fs.readFile(process.argv[3], function (err, data) {
  if (err) {
    return;
  }
  fs.appendFile(process.argv[4], data, {});
});
