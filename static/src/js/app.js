var React = require('react');
var ProjectImages = require('./components/project-images');


$(window).load(function(){
    $(window).trigger('scroll').trigger('resize');
    var s = skrollr.init();
});

React.render(<ProjectImages />, document.getElementById('project-images'));