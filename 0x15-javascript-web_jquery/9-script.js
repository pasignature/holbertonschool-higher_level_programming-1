// Fetches and prints how to say hello
$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  dataType: 'json',
  success: function (data) {
    let hi = 'hello';
    if ($('HTML')[0].lang === 'fr') {
      hi = data.hello;
    }
    $('DIV#hello').text(hi);
  }
});
