#!/usr/bin/node

const url = process.argv[2];
const filename = process.argv[3];
const request = require('request');
const fs = require('fs');

request(url, function (error, response, content) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filename, content, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  } else {
    console.log('Status Code: ' + response.statusCode);
  }
});
