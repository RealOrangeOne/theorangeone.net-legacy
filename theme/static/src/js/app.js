'use strict';

require('./creative');
var ansi_up = require('ansi_up');


$('.image').each(function () {  // setup div-image hybrids
  var ele = $(this);
  if (ele.data('image')) {
    ele.css('background-image', 'url(' + ele.data('image') + ')');
  } else {
    ele.removeClass('image');
  }
});

$('.ansi-up').each(function () {
  var ele = $(this);
  ele.html(ansi_up.ansi_to_html(ele.html()));
});
