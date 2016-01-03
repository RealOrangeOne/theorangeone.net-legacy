/* global $ */

import './events.js';

import React from 'react';
import ProjectImagesTypes from './components/index/project-images-types';
import ProjectImagesMain from './components/index/project-images-main';


if ($('body').hasClass('index')) {  // Render components on index
  React.render(<ProjectImagesTypes />, document.getElementById('project-images-types'));
  React.render(<ProjectImagesMain />, document.getElementById('project-images-main'));
}
