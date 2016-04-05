/* global $ */

import './events.js';
import './globals.js';

import 'whatwg-fetch';

import React from 'react';

import NavBar from './components/navbar/navbar';
import Breadcrumbs from './components/breadcrumbs';


if ($('navbar').length > 0) {
  React.render(<NavBar />, $('navbar')[0]);
}

if ($('#breadcrumbs').length > 0) {
  React.render(<Breadcrumbs />, $('#breadcrumbs')[0]);
}

if ($('.header h1').text()) {
  $('.markdown-content h1').eq(0).hide();
}
