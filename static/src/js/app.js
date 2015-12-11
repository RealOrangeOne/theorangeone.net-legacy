/* global $ */

require('./utils.js');

var React = require('react');
var ProjectImagesTypes = require('./components/index/project-images-types');
var ProjectImagesMain = require('./components/index/project-images-main');

if ($('body').hasClass('index')) {  // Render components on index
  React.render(<ProjectImagesTypes />, document.getElementById('project-images-types'));
  React.render(<ProjectImagesMain />, document.getElementById('project-images-main'));
}
