import React from 'react';

export default class DropdownItem extends React.Component {
  render() {
    return (
      <li><a href={this.props.href}><i className={'icon ' + this.props.icon}></i> {this.props.children}</a></li>
    );
  }
}
