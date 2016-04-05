import React from 'react';

export default class Breadcrumbs extends React.Component {
  render() {
    const loc = location.pathname.endsWith('/') ? location.pathname.slice(0, -1) : location.pathname;
    const urlParts = Object.freeze(loc.split('/').slice(1));
    if (urlParts.length < 2) {
      return null;
    }
    var elements = [];
    for (var i = 0; i < urlParts.length; i++) {
      var dirs = [];
      for (var j = 0; j <= i; j++) {
        dirs.push(urlParts[j]);
      }
      if (i === (urlParts.length - 1)) {
        elements.push(
          <li className="active">{urlParts[i]}</li>
        );
      } else {
        var url = '/' + dirs.join('/') + '/';
        elements.push(
          <li><a href={url}>{urlParts[i]}</a></li>
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
