#!/usr/bin/node
// Writes a page to a file
require('request').get(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    require('fs').writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
