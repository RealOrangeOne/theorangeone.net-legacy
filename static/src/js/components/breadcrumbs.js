import React from 'react';

export default class Breadcrumbs extends React.Component {
  constructor() {
    super();
    this.urlParts = Object.freeze(location.pathname.split('/').slice(1, -1));
  }

  render() {
    if (this.urlParts.length < 2) {
      return;
    }
    var elements = [];
    for (var i = 0; i < this.urlParts.length; i++) {
      var dirs = [];
      for (var j = 0; j <= i; j++) {
        dirs.push(this.urlParts[j]);
      }
      if (i === (this.urlParts.length - 1)) {
        elements.push(
          <li className="active" href={url}>{this.urlParts[i]}</li>
        );
      } else {
        var url = '/' + dirs.join('/') + '/';
        elements.push(
          <li><a href={url}>{this.urlParts[i]}</a></li>
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
