#!/usr/bin/node
// imports a dict of occ by user id and computes dict of user id by occ
let data = require('./101-data').dict;
let dict = {};
for (let [k, v] of Object.entries(data)) {
  if (dict[v] === undefined) {
    dict[v] = [];
  }
  dict[v].push(k);
}
console.log(dict);
