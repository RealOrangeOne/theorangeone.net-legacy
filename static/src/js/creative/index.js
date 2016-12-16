import WOW from 'wow.js';
import { NAVBAR_HEIGHT, SCROLL_SPEED } from '../consts';

new WOW().init();

/*!
 * Start Bootstrap - Creative Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 * (Edited for theorangeone.net)
 */



$('a.page-scroll').bind('click', function(event) {
  const anchor = $(this);
  $('html, body').stop().animate(
    { scrollTop: ($(anchor.attr('href')).offset().top - NAVBAR_HEIGHT) },
    SCROLL_SPEED
  );
  event.preventDefault();
});


// Highlight the top nav as scrolling occurs
$('body').scrollspy({
  target: '.navbar-fixed-top',
  offset: NAVBAR_HEIGHT + 1
});

// Closes the Responsive Menu on Menu Item Click
$('.navbar-collapse ul li a').click(function() {
  $('.navbar-toggle:visible').click();
});

// Offset for Main Navigation
$('#main-nav').affix({
  offset: {
    top: NAVBAR_HEIGHT * 1.5
  }
});
