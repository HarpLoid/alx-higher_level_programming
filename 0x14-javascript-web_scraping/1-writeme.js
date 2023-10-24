#!/usr/bin/node

const fs = require('fs');

let file_path = process.argv[2];
let content = process.argv[3];

fs.writeFile(file_path, content, 'utf8', (error) => {
  if (error) {
    console.log(error);
  }
});
