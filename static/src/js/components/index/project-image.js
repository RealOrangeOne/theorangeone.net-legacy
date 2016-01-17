import React from 'react';
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
      return;
    }
    fetch('/reverse/', {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        ident: this.props.data.link,
      })
    }).then(function (response) {
      if (response.status === 302) {
        this.setState({ url: response.json() });
        return response;
      } else {
        var error = new Error(response.statusText);
        error.response = response;
        throw error;
      }
    }.bind(this)).catch((e) => console.log(e));
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
