#!/usr/bin/node
// Searches for second biggest number

let size = process.argv.length;
if (size <= 3) {
  console.log('0');
} else {
  let args = process.argv.sort().reverse();
  console.log(args[1]);
}
