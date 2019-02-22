// Fetches and replaces the name of a URL
$.ajax({
  url: 'https://swapi.co/api/people/5/?format=json',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    $('div#character').text(data.name);
  }
});
