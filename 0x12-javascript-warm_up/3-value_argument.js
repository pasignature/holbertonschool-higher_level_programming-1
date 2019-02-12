#!/usr/bin/node
// Prints 3 lines to the screen

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
