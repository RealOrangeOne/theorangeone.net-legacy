var React = require('react');
var ReactBootstrap = require('react-bootstrap');
var Row = ReactBootstrap.Row;
var Col = ReactBootstrap.Col;

var projectImage = React.createClass({
  render: function () {
    var contents = this.props.isHovered ? 
    (
      <div className="animated zoomIn">
        <h4>{this.props.data.title}</h4>
        <p>{this.props.data.text}</p>
        <a href={this.props.data.link} className="btn btn-default">
          Find out more
        </a> 
      </div>    
    ) : null;
    return (
      <Col sm={4}>
        <div className="wrapper" >
          <div className={"project " + this.props.data.className} 
            onMouseOver={this.props.onHover}
            onMouseLeave={this.props.onLeave} >
            { contents }            
          </div>
        </div>
      </Col>
    );
  }
});

module.exports = projectImage;