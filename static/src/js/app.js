var React = require('react');
var ProjectImages = require('./components/project-images');

window.scrollToElement = function(ident) {
  $('html, body').animate({scrollTop: $(ident).offset().top}, 1000);
}

$(window).load(function(){
    $(window).trigger('scroll').trigger('resize');
});

React.render(<ProjectImages />, document.getElementById('project-images'));