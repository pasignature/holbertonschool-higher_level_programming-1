#!/usr/bin/node
// imports a dict of occ by user id and computes dict of user id by occ
let dict = require('./101-data').dict;
for (let [k, v] of Object.entries(dict)) {
  if (dict[v] === undefined) {
    dict[v] = [];
  }
  dict[v].push(k);
  delete dict[k];
}
console.log(dict);
