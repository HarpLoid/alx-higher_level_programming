#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, content) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let films = JSON.parse(content).results;
    let count = 0;
    for (let film in films) {
      let chars = films[film].characters;
      for (let char in chars) {
        if (chars[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('Status Code: ' + response.statusCode);
  }
});
