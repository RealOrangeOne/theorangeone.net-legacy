'use strict';

var WOW = require('wow.js');
var consts = require('../consts');

new WOW().init();

/*!
 * Start Bootstrap - Creative Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 * (Edited for theorangeone.net)
 */

// jQuery for page scrolling feature
$('a.page-scroll').bind('click', function(event) {
  $('html, body').stop().animate(
    { scrollTop: $($(this).attr('href')).offset().top - consts.NAVBAR_HEIGHT },
    consts.SCROLL_SPEED
  );
  event.preventDefault();
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
  target: '.navbar-fixed-top',
  offset: consts.NAVBAR_HEIGHT + 1
});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
  $('.navbar-toggle:visible').click();
});


// Offset for Main Navigation
$('#main-nav').affix({
  offset: {
    top: consts.NAVBAR_HEIGHT * 1.5
  }
});
