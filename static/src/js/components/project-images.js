var React = require('react');

const projectData = [
  {key: 1, title: "College", info: "", link: ""},
  {key: 2, title: "Personal", info: "", link: ""},
  {key: 3, title: "Work", info: "", link: ""}
];


var projectImages = React.createClass({
  getInitialState: function () {
    return {
      hover: 0,
    };
  },

  setHovering: function (key, evt) {
    this.setState({hover: key});
  },
  render: function () {
    var isHovered;
    var projectTiles = projectData.map(function (project) {
      isHovered = (project.key == this.state.hover);
      return (
        <div className="col-sm-4">

        </div>
      );
    });
    return (
      <div className="container">
        <div className="panel panel-default">
          <div className="panel-body row">
            { projectTiles }
          </div>
        </div>
      </div>
    );
  }
});

module.exports = projectImages;