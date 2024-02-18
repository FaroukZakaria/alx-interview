#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(movieUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const characters = body.characters;

  characters.forEach(characterUrl => {
    request(characterUrl, { json: true }, (error, response, characterBody) => {
      if (error) {
        console.error(error);
        return;
      }
      console.log(characterBody.name);
    });
  });
});

