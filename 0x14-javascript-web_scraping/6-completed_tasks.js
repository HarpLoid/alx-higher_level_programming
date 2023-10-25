#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, content) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(content);
    const dict = {};
    for (const todo in todos) {
      if (todos[todo].completed) {
        if (dict[todos[todo].userId] === undefined) {
          dict[todos[todo].userId] = 1;
        } else {
          dict[todos[todo].userId]++;
        }
      }
    }
    console.log(dict);
  } else {
    console.log('Status Code: ' + response.statusCode);
  }
});
