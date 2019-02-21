#!/usr/bin/node
// Computes the number of tasks completed by id
require('request').get(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let tasks = JSON.parse(body);
    let res = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        if (!(tasks[i].userId in res)) {
          res[tasks[i].userId] = 0;
        }
        res[tasks[i].userId] += 1;
      }
    }
    console.log(res);
  }
});
