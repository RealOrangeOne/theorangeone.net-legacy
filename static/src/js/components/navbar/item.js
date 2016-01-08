import React from 'react';

export default class Item extends React.Component {
  render() {
    let icon;
    if (this.props.icon) {
      icon = (
        <i className={'icon ' + this.props.icon}></i>
      );
    }
    return (
      <li><a href={this.props.href}>{icon}{this.props.children}</a></li>
    );
  }
}
