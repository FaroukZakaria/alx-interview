#!/usr/bin/node
const util = require('util');
const req = util.promisify(require('request'));
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

(async () => {
  try {
    const body = (await req(url)).body;
    const MovieCharacters = JSON.parse(body).characters;
    for (const character of MovieCharacters) {
      const body = (await req(character)).body;
      const CharacterName = JSON.parse(body).name;
      console.log(CharacterName);
    }
  } catch (error) {
    console.log(error);
  }
})();
