import React from 'react';
var ReactBootstrap = require('react-bootstrap');
var Col = ReactBootstrap.Col;

export default class ProjectImage extends React.Component {
  render() {
    var animationClass = this.props.isHovered ? 'zoomIn' : 'zoomOut';
    var classes = this.props.data.title.toLowerCase().replace(' ', '-');
    return (
      <Col sm={4} className="project-image">
        <div className={'wrapper ' + classes}>
          <div className="project"
            onMouseOver={this.props.onHover}
            onMouseLeave={this.props.onLeave} >
            <div className={'animated ' + animationClass}>
              <h4>{this.props.data.title}</h4>
              <p>{this.props.data.text}</p>
              <a href={this.props.data.link} className="btn btn-default btn-small">
                Find out more
              </a>
            </div>
          </div>
        </div>
      </Col>
    );
  }
}
