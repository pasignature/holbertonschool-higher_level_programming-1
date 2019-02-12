#!/usr/bin/node
// Prints text based on input arg

let number = parseInt(process.argv[2]);
if (number) {
  console.log('My number: ' + number);
} else {
  console.log('Not a number');
}
