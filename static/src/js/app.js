var React = require('react');
var indexCarousel = require('./components/indexCarousel.js');

require('./events.js');


if ($('#index-carousel-container').length == 1) {
    React.render(indexCarousel, $("#index-carousel-container")[0]);
}

$(window).load(function(){
    $(window).trigger('scroll').trigger('resize');
    var s = skrollr.init();
});