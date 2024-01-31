#!/usr/bin/node

// Importing the 'request' module for making HTTP requests
const request = require('request');

// Function to retrieve data from a given URL using a Promise
function getDataFrom(url) {
  return new Promise(function (resolve, reject) {
    // Making an HTTP GET request using the 'request' module
    request(url, function (err, _res, body) {
      if (err) {
        // Rejecting the Promise with an error if the request fails
        reject(err);
      } else {
        // Resolving the Promise with the response body if the request is successful
        resolve(body);
      }
    });
  });
}

// Function to handle errors by logging them to the console
function errHandler(err) {
  console.log(err);
}

// Function to print characters from a Star Wars movie based on the provided movie ID
function printMovieCharacters(movieId) {
  // Constructing the URL for the Star Wars movie API endpoint
  const movieUri = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  // Fetching data from the movie API endpoint
  getDataFrom(movieUri)
    .then(JSON.parse, errHandler) // Parsing the JSON response or handling errors
    .then(function (res) {
      const characters = res.characters;
      const promises = [];

      // Creating an array of promises for fetching data from each character endpoint
      for (let i = 0; i < characters.length; ++i) {
        promises.push(getDataFrom(characters[i]));
      }

      // Resolving all promises in parallel using Promise.all
      Promise.all(promises)
        .then((results) => {
          // Extracting and printing the names of characters from the results
          for (let i = 0; i < results.length; ++i) {
            console.log(JSON.parse(results[i]).name);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    });
}

// Calling the function with the movie ID provided as a command-line argument
printMovieCharacters(process.argv[2]);
