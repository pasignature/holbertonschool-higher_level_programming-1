#!/usr/bin/node
// Searches for second biggest number

let size = process.argv.length;
if (size <= 1) {
  console.log('0');
} else {
  let args = process.argv.slice(2);
  console.log(args.sort()[size - 4]);
}
