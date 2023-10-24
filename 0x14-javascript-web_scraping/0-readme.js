#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', function (error, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(body);
  }
});
