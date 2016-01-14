import React from 'react';
var ReactBootstrap = require('react-bootstrap');
import ProjectImage from './project-image';
var Row = ReactBootstrap.Row;

const DATA = [
  {
    title: 'Custom PC',
    text: 'My time at college was where I learnt most about programming, and discovered my skill and passion for it.',
    link: '',
  },
  {
    title: 'Personal',
    text: 'I write code just to write code, but sometimes it serves a purpose.',
    link: '',
  },
  {
    title: 'Work',
    text: 'I\'m an apprentice software developer at Dabapps, and this is what I\'ve done.',
    link: '',
  },
  {
    title: 'College',
    text: 'My time at college was where I learnt most about programming, and discovered my skill and passion for it.',
    link: '',
  },
  {
    title: 'Personal',
    text: 'I write code just to write code, but sometimes it serves a purpose.',
    link: '',
  },
  {
    title: 'Work',
    text: 'I\'m an apprentice software developer at Dabapps, and this is what I\'ve done.',
    link: '',
  }
];

export default class ProjectImagesMain extends React.Component {
  constructor() {
    super();
    this.keys = [[1, 2, 3], [4, 5, 6]];
    this.state = {
      hover: 0
    };
    this.setHovering = this.setHovering.bind(this);
  }
  setHovering(key) {
    this.setState({hover: key});
  }
  render() {
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
}
