#!/usr/bin/node
// displays status code of a get request
require('request').get(process.argv[2], function(err, res) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + res.statusCode);
  }
});
