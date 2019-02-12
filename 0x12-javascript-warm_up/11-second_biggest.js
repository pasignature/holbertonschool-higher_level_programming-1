#!/usr/bin/node
// Searches for second biggest number

let arr = [];
if (process.argv.length < 4) {
  console.log(0);
} else {
  for (let i = 0; i < process.argv.length; i++) {
    if (parseInt(process.argv[i])) {
      arr.push(parseInt(process.argv[i]));
    }
  }
  arr = [...new Set(arr)].sort((a, b) => a - b);
  if (arr.length === 1) {
    console.log(arr[0]);
  } else {
    arr.pop();
    console.log(arr.pop());
  }
}
