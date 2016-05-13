import React from 'react';


export default class Item extends React.Component {
  render() {
    const href = this.props.href.endsWith('/') ? this.props.href : this.props.href + '/';
    let icon;
    if (this.props.icon) {
      if (this.props.icon.startsWith('ion')) {
        icon = (
          <i className={'icon ' + this.props.icon} />
        );
      } else if (this.props.icon.startsWith('glyphicon')) {
        icon = (
          <span className={'glyphicon ' + this.props.icon} aria-hidden="true" />
        );
      }
    }
    return (
      <li><a href={href}>{icon}{this.props.children}</a></li>
    );
  }
}
