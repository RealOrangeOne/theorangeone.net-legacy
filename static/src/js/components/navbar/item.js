import React from 'react';
import Reverser from '../../helpers/reverser';


export default class Item extends React.Component {
  constructor() {
    super();
    this.state = {
      url: '#'
    };
  }

  componentDidMount() {
    if (!this.props.href && !this.props.ident) {
      return;
    }

    if (this.props.href) {
      this.setState({url: this.props.href});
    } else {
      Reverser(this.props.ident, this.props.args, function (url) {
        this.setState({ url });
      }.bind(this));
    }
  }
  render() {
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
      <li><a href={this.state.url}>{icon}{this.props.children}</a></li>
    );
  }
}
