#!/usr/bin/node
// Prints a square

let size = parseInt(process.argv[2]);
if (size) {
  for (let y = 0; y < size; y++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
