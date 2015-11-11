var React = require('react');
var ReactBootstrap = require('react-bootstrap');
var Row = ReactBootstrap.Row;
var ProjectImage = require('./project-image');

const DATA = [
  {
    className: "college",
    title: "College",
    text: "In my life as a student, I wrote a lot of code!",
    link: "",
  },
  {
    className: "personal",
    title: "Personal",
    text: "All the stuff I've written on my own time",
    link: "",
  },
  {
    className: "work",
    title: "Work",
    text: "I'm an apprentice software developer at Dabapps, and this is what I've done.",
    link: "",
  }
];


var projectImages = React.createClass({
  keys: [1,2,3],
  getInitialState: function () {
    return {
      hover: 0,
    };
  },

  setHovering: function (key, evt) {
    this.setState({hover: key});
  },
  render: function () {
    var images = this.keys.map(function (key) {
      return (
        <ProjectImage isHovered={this.state.hover == key} 
          data={DATA[key - 1]} 
          onHover={this.setHovering.bind(this, key)} 
          onLeave={this.setHovering.bind(this, 0)} />
        );
    }.bind(this));
    return (
      <div className="container">
        <h1>Projects</h1>
        <Row>
          { images }
        </Row>
      </div>
    );
  }
});

module.exports = projectImages;