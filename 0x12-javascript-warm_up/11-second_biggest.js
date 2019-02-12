#!/usr/bin/node
// Searches for second biggest number

let size = process.argv.length;
if (size <= 3) {
  console.log('0');
} else {
  let first = process.argv[2];
  let sec = process.argv[2] - 1;
  for (let i = 2; i < size; i++) {
    if (process.argv[i] > first) {
      sec = first;
      first = process.argv[i];
    } else {
      if (process.argv[i] > sec) {
	sec = process.argv[i];
      }
    }
  }
  console.log(sec);
}
