#!/usr/bin/node

const fs = require('fs');

let file_path = process.argv[2];

fs.readFile(file_path, 'utf8', function (error, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(body);
  }
});
