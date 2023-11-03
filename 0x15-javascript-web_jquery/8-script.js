/**
 * fetches and lists the title for all movies
 * by using this
 * URL: https://swapi-api.alx-tools.com/api/films/?format=json
 */

$.getJSON(
  'https://swapi-api.alx-tools.com/api/films/?format=json',
  function (data, stats) {
    if (stats === 'success') {
      const films = data.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  }
);
