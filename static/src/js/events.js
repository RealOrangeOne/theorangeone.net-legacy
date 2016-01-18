/* global $ */
var is_navbar_attached = false;

$(window).load(function() {
  $(window).trigger('scroll');
  $.material.init()
});

function detach_navbar() {
  $('#navbar-container').removeClass('stick-top').addClass('align');
  $('.dropdown-menu').removeClass('dropdown').addClass('dropup');
}

function attach_navbar() {
  $('#navbar-container').removeClass('align').addClass('stick-top');
  $('.dropdown-menu').removeClass('dropup').addClass('dropdown');
}

function flip_dropdowns(obj, direction) {
  if (obj.hasClass('drop' + direction)) { return; }
  var reverse = ((direction === 'up') ? 'down' : 'up');
  obj.removeClass('drop' + reverse).addClass('drop' + direction);
  obj.prev().find('i').removeClass('ion-ios-arrow-' + reverse).addClass('ion-ios-arrow-' + direction);
}

function position_navbar() {
  if ($(window).width() < 862) {  // @screen-sm
    $('.navbar-icon').removeClass('ion-ios-arrow-up').addClass('ion-ios-arrow-down');
    return;
  }
  if ($(window).scrollTop() > $('#navbar-anchor').offset().top) {
    if (!is_navbar_attached) {
      attach_navbar();
      is_navbar_attached = true;
    }
  } else if (is_navbar_attached) {
    detach_navbar();
    is_navbar_attached = false;
  }
  $('.dropdown-menu').each(function() {
    var direction = ($(this).height() + 10 < $('nav').offset().top - $(window).scrollTop()) ? 'up' : 'down';
    flip_dropdowns($(this), direction);
  });
}

$(function() { // https://css-tricks.com/snippets/jquery/smooth-scrolling/
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '')
      && location.hostname === this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});

$('a[href="soon"]').click(function (e) {
  e.preventDefault();
  alert('Content coming soon, stand by!');
});

$(window).scroll(position_navbar);
