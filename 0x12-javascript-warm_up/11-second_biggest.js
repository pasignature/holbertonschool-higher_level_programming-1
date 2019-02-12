#!/usr/bin/node
// Searches for second biggest number

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let tmp =process.argv.slice(2).map(function(v) {
    return parseInt(v);
  });
  let arr = [...new Set(tmp)].sort().reverse();
  if (arr.length === 1) {
    console.log(arr[0]);
  } else {
    console.log(arr[1]);
  }
}
