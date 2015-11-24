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
    link: '',
  },
  {
    className: 'work',
    title: 'Work',
    text: 'I\'m an apprentice software developer at Dabapps, and this is what I\'ve done.',
    link: '',
  },
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
    link: '',
  },
  {
    className: 'work',
    title: 'Work',
    text: 'I\'m an apprentice software developer at Dabapps, and this is what I\'ve done.',
    link: '',
  }
];


var projectImagesMain = React.createClass({
  keys: [[1, 2, 3], [4, 5, 6]],
  getInitialState: function () {
    return {
      hover: 0,
    };
  },

  setHovering: function (key) {
    this.setState({hover: key});
  },
  render: function () {
    var generate_image = function (key) {
      return (
        <ProjectImage isHovered={this.state.hover === key}
          data={DATA[key - 1]}
          onHover={this.setHovering.bind(this, key)}
          onLeave={this.setHovering.bind(this, 0)} />
        );
    }.bind(this);
    var images = this.keys.map( function (keyColumns) {
      var col = keyColumns.map(function (key) {
        return generate_image(key);
      });
      return (<Row>{col}</Row>);
    });
    return (
      <div className="container">
        <h1>Personal Projects</h1>
        { images }
      </div>
    );
  }
});

module.exports = projectImagesMain;
