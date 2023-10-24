#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request(url, function (error, response, content) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    content = JSON.parse(content);
    console.log(content.title);
  } else {
    console.log('Status Code: ' + response.statusCode);
  }
});
