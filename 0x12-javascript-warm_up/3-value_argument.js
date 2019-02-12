#!/usr/bin/node
// Prints 3 lines to the screen

let size = parseInt(process.argv.length);
if (size === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
