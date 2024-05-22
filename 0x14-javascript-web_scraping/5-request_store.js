#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
const fs = require('fs');

request.get(url, (error, responce, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
