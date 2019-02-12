#!/usr/bin/node
// Searches for second biggest number

let args = process.argv.slice(2);
if (args.length <= 1) {
  console.log('0');
} else {
  console.log(args.sort()[args.length - 2]);
}
