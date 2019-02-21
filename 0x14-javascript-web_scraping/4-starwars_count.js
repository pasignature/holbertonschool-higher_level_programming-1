#!/usr/bin/node
// prints the title of a SW movie where the eps # matches a given int
require('request').get(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      let chars = films[i].characters;
      for (let j = 0; j < chars.length ; j++ )
      {
	if (chars[j].includes('/18/')) {
	  count++;
	  break;
	}
      }
    }
    console.log(count);
  }
});
