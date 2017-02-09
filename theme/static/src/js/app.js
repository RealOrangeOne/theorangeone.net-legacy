'use strict';

require('./creative');
var ansi_up = require('ansi_up');
var consts = require('./consts');


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


$('.navbar-brand').bind('click', function (event) {
  if ($('html').scrollTop() > consts.NAVBAR_HEIGHT) {
    $('html, body').stop().animate({
      scrollTop: 0
    }, consts.SCROLL_SPEED);
  } else {
    window.location = '/';
  }
  event.preventDefault();
});

$('.panel-heading').bind('click', function () {
  var ele = $(this);
  if (ele.find('.panel-body').hasClass('ascii-hidden')) {
    ele = ele.find('.panel-body');
    var raw_code = ele.text().split(' ');

  }
});

$('.protected-mailto').bind('click', function (evt) {
  evt.preventDefault();
  var char_codes = $(this).data('value').split(' ');
  var plain_text = []
  for(var i=0; i<char_codes.length; i++) {
    plain_text.push(String.fromCharCode(parseInt(char_codes[i])));
  }
  window.location = 'mailto:' + plain_text.join('');
});
