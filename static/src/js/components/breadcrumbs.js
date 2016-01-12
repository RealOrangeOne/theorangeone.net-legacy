import React from 'react';

let {
  Breadcrumb,
  BreadcrumbItem
} = require('react-bootstrap');

export default class Breadcrumbs extends React.Component {
  render() {
    const parts = location.pathname.split('/').slice(1, -1);
    var elements = [];
    for (var i = 0; i < parts.length; i++) {
      var dirs = [];
      for (var j = 0; j <= i; j++) {
        dirs.push(parts[j]);
      }
      if (i === (parts.length - 1)) {
        elements.push(
          <li className="active" href={url}>
            {parts[i]}
          </li>
        );
      } else {
        var url = '/' + dirs.join('/') + '/';
        elements.push(
          <li>
            <a href={url}>
              {parts[i]}
            </a>
          </li>
        );
      }
    }
    return (
      <ol className="breadcrumb">
        { elements }
      </ol>
    );
  }
}
