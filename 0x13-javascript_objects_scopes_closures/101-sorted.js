#!/usr/bin/node
// imports a dict of occ by user id and computes dict of user id by occ
let data = require('./101-data').dict;
for (let [k, v] of Object.entries(data)) {
  if (data[v] === undefined) {
    data[v] = [];
  }
  data[v].push(k);
  delete data[k];
}
console.log(data);
