/**
 * Toggles the class of the <header> element
 * when the user clicks on the tag DIV#toggle_header
 */

$('DIV#toggle_header').addClass('red');

$('DIV#toggle_header').on('click', function () {
  if ($('#toggle_header').hasClass('red')) {
    $('#toggle_header').removeClass('red');
    $('#toggle_header').addClass('green');
  } else {
    $('#toggle_header').removeClass('green');
    $('#toggle_header').addClass('red');
  }
});
