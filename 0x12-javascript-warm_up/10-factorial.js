#!/usr/bin/node
// Computes and prints a factorial

function fac (a) {
  if (isNaN(a) || a <= 1) {
    return 1;
  } else {
    return a * fac(a - 1);
  }
}
console.log(fac(parseInt(process.argv[2])));
