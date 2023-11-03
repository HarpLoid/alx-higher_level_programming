/**
 * adds a <li> element to a list when
 * the user clicks on the tag DIV#add_item
 */

$('DIV#add_item').on('click', function () {
  $('.my_list').append('<li>Item</li>');
});
