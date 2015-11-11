var React = require('react');
var ReactBootstrap = require('react-bootstrap');
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;

var projectImage = React.createClass({
  render: function () {
    var animationClass = this.props.isHovered ? 'zoomIn' : 'zoomOut';
    return (
      <Col sm={4}>
        <div className={"wrapper " + this.props.data.className}>
          <div className="project" 
            onMouseOver={this.props.onHover}
            onMouseLeave={this.props.onLeave} >
            <div className={"animated " + animationClass}>
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
});

module.exports = projectImage;