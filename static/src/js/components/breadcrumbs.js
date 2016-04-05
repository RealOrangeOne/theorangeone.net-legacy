import React from 'react';

export default class Breadcrumbs extends React.Component {
  render() {
    const urlParts = Object.freeze(location.pathname.split('/').slice(1, -1));
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
