import React from 'react';
import Reverser from '../../helpers/reverser';
var ReactBootstrap = require('react-bootstrap');
var Col = ReactBootstrap.Col;

export default class ProjectImage extends React.Component {
  constructor() {
    super();
    this.state = {
      url: ''
    };
  }
  componentDidMount() {
    if (this.props.data.link.startsWith('#')) {
      this.setState({url: this.props.data.link});
    } else {
      const args = this.props.data.args || false;
      Reverser(this.props.data.link, args)
      .then(function (url) {
        this.setState({ url });
      }.bind(this))
      .catch(console.log);
    }
  }

  render() {
    var animationClass = this.props.isHovered ? 'zoomIn' : 'zoomOut';
    var classes = this.props.data.title.toLowerCase().replace(/ /g, '-');
    return (
      <Col sm={4} className="project-image">
        <div className={'wrapper ' + classes}>
          <div className="project"
            onMouseOver={this.props.onHover}
            onMouseLeave={this.props.onLeave} >
            <div className={'animated ' + animationClass}>
              <h4>{this.props.data.title}</h4>
              <p>{this.props.data.text}</p>
              <a href={this.state.url} className="btn btn-default btn-small">
                Find out more
              </a>
            </div>
          </div>
        </div>
      </Col>
    );
  }
}
