var React = require('react');

$(window).load(function(){
    $(window).trigger('scroll').trigger('resize');
    var s = skrollr.init();
});