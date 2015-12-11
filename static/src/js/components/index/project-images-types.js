var React = require('react');
var ReactBootstrap = require('react-bootstrap');
var Row = ReactBootstrap.Row;
var ProjectImage = require('./project-image');

const DATA = [
  {
    className: 'college',
    title: 'College',
    text: 'My time at college was where I learnt most about programming, and discovered my skill and passion for it.',
    link: '',
  },
  {
    className: 'personal',
    title: 'Personal',
    text: 'I write code just to write code, but sometimes it serves a purpose.',
    link: '#project-images-main',
  },
  {
    className: 'work',
    title: 'Work',
    text: 'I\'m an apprentice software developer at Dabapps, and this is what I\'ve done.',
    link: '',
  }
];


var projectImagesTypes = React.createClass({
  keys: [1, 2, 3],
  getInitialState: function () {
    return {
      hover: 0,
    };
  },

  setHovering: function (key) {
    this.setState({hover: key});
  },
  render: function () {
    var images = this.keys.map(function (key) {
      return (
        <ProjectImage isHovered={this.state.hover === key}
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

module.exports = projectImagesTypes;
