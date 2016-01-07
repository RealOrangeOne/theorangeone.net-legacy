import React from 'react';

export default class Header extends React.Component {
  render() {
    const items = [0, 1, 2];
    var iconBars = items.map(function (item) {
      return (
        <span className="icon-bar" key={item} />
      );
    });
    return (
      <div className="navbar-header">
        <button type="button"
          className="navbar-toggle collapsed"
          data-toggle="collapse"
          data-target="#navbar"
          aria-expanded="false" >
          <span className="sr-only">Toggle navigation</span>
          {{ iconBars }}
        </button>
        <a className="navbar-brand visible-xs">
          <i className="icon ion-compass" />
          Navigation
        </a>
      </div>
    );
  }
}
