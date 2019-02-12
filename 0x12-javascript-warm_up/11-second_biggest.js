#!/usr/bin/node
// Searches for second biggest number

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let arr = [...new Set(process.argv.slice(2))].sort().reverse();
  if (arr.length === 1) {
    console.log(arr[0]);
  } else {
    console.log(arr[1]);
  }
}
