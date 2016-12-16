import './creative';
import ansi_up from 'ansi_up';
import { SCROLL_SPEED, NAVBAR_HEIGHT } from './consts';

$('.image').each(function () {  // setup div-image hybrids
  const ele = $(this);
  if (ele.data('image')) {
    ele.css('background-image', 'url(' + ele.data('image') + ')');
  } else {
    ele.removeClass('image');
  }
});

$('.ansi-up').each(function () {
  const ele = $(this);
  ele.html(ansi_up.ansi_to_html(ele.html()));
});


$('.navbar-brand').bind('click', function (event) {
  if ($('html').scrollTop() > NAVBAR_HEIGHT) {
    $('html, body').stop().animate({
      scrollTop: 0
    }, SCROLL_SPEED);
  } else {
    window.location = '/';
  }
  event.preventDefault();
});
