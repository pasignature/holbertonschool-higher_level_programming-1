#!/usr/bin/node
// imports a dict of occ by user id and computes dict of user id by occ
let dict = require('./101-data').dict;
let tmp = {};
for (let k in dict) {
  if (tmp[dict[k]] === undefined) {
    tmp[dict[k]] = [];
  }
  tmp[dict[k]].push(k);
}
console.log(tmp);
