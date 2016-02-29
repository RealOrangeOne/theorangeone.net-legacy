import React from 'react';

export default class Dropdown extends React.Component {
  render() {
    return (
      <li className="dropdown">
        <a className="dropdown-toggle"
          data-toggle="dropdown"
          role="button"
          aria-haspopup="true"
          aria-expanded="false">
          { this.props.title } <i className="icon ion-ios-arrow-up navbar-icon h4 hidden-sm"></i>
        </a>
        <ul className="dropdown-menu dropup">
          { this.props.children }
        </ul>
      </li>
    );
  }
}
