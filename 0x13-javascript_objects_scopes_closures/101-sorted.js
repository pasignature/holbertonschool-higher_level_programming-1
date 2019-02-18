#!/usr/bin/node
// imports a dict of occ by user id and computes dict of user id by occ
let dict = require('./101-data').dict;
for (let k in dict) {
  if (dict[dict[k]] === undefined) {
    dict[dict[k]] = [];
  }
  dict[dict[k]].push(k);
  delete dict[k];
}
console.log(dict);
