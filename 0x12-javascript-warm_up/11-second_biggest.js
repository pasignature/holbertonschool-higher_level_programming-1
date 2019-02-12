#!/usr/bin/node
// Searches for second biggest number

if (process.argv.length < 3) {
  console.log('0');
} else {
  let arr = process.argv.splice(2).sort();
  arr.pop();
  console.log(arr.pop());
}
