#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    process.exit(1);
  }

  const movie = JSON.parse(body);

  if (!movie) {
    console.error('Movie not found.');
    process.exit(1);
  }

  movie.characters.forEach(characterUrl => {
    request(characterUrl, (error, response, characterBody) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      const character = JSON.parse(characterBody);
      console.log(character.name);
    });
  });
});
