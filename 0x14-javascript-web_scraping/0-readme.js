#!/usr/bin/node
// Reads and prints a file
let fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
