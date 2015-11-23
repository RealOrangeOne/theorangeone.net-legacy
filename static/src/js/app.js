var React = require('react');
var ProjectImagesTypes = require('./components/project-images-types');
var ProjectImagesMain = require('./components/project-images-main');

$(function() { // https://css-tricks.com/snippets/jquery/smooth-scrolling/
  $('a[href*=#]:not([href=#])').click(function() {
    if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
      if (target.length) {
        $('html,body').animate({
          scrollTop: target.offset().top
        }, 1000);
        return false;
      }
    }
  });
});

$(window).load(function(){
    $(window).trigger('scroll').trigger('resize');
});

React.render(<ProjectImagesTypes />, document.getElementById('project-images-types'));
React.render(<ProjectImagesMain />, document.getElementById('project-images-main'));
