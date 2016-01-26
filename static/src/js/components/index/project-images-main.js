import React from 'react';
var ReactBootstrap = require('react-bootstrap');
import ProjectImage from './project-image';
var Row = ReactBootstrap.Row;

const DATA = [
  {
    title: 'Custom PC',
    text: 'Without my PCs, I wouldnt be able to do anything you see here.',
    link: 'about:me',
  },
  {
    title: 'BSOD-Enabler',
    text: 'Ever wanted to bring up a Blue Screen of Death on command, well now you can!',
    link: '',
  },
  {
    title: 'Yoga Pal',
    text: 'For anyone running a 2-in-1 laptop on an OS other than Windows.',
    link: '',
  },
  {
    title: 'Attack on Blocks',
    text: 'The closest thing I\'ve done to games development',
    link: '',
  },
  {
    title: 'Dotfile-automator',
    text: 'Automatically sync your dotfiles between machines. Keep things just the way you like them!',
    link: '',
  },
  {
    title: 'Student Robotics',
    text: '',
    link: 'robotics:index',
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
    this._generate_image = this._generate_image.bind(this);
  }

  setHovering(key) {
    this.setState({hover: key});
  }

  _generate_image(key) {
    return (
      <ProjectImage
        isHovered={this.state.hover === key}
        data={DATA[key - 1]}
        onHover={this.setHovering.bind(this, key)}
        onLeave={this.setHovering.bind(this, 0)} />
      );
  }

  render() {
    var images = this.keys.map(function (keyColumns) {
      var col = keyColumns.map(function (key) {
        return this._generate_image(key);
      }.bind(this));
      return (<Row>{col}</Row>);
    }.bind(this));
    return (
      <div className="container">
        <h1>Personal Projects</h1>
        { images }
      </div>
    );
  }
}
