#!/usr/bin/node
// Searches for second biggest number

if (process.argv.length <= 3) {
  console.log('0');
} else {
  console.log([...new Set(process.argv.slice(2))].sort().reverse()[1]);
}
