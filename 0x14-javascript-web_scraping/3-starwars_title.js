#!/usr/bin/node
// prints the title of a SW movie where the eps # matches a given int
require('request').get('http://swapi.co/api/films/' + process.argv[2] + '/', function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
