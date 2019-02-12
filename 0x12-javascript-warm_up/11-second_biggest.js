#!/usr/bin/node
// Searches for second biggest number

if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log('0');
} else {
  console.log(process.argv.sort().reverse()[1]);
}
