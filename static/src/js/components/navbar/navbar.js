import React from 'react';
import Header from './header';
import Dropdown from './dropdown';
import DropdownItem from './dropdown-item';
var NavItem = require('react-bootstrap').NavItem;

export default class NavBar extends React.Component {
  render() {
    return (
      <span>
        <div id="navbar-anchor" />
        <div id="navbar-container" className="align h4">
          <nav className="navbar navbar-inverse">
            <div className="container-fluid">
              <Header />
              <div className="collapse navbar-collapse" id="navbar">
                <ul className="nav navbar-nav home-button hidden-sm">
                  <li className="active home"><a href=""><i className="icon ion-home"></i></a></li>
                </ul>
                <ul className="nav navbar-nav" id="navigation">
                  <Dropdown title="Projects">
                    <DropdownItem href="#" icon="ion-social-freebsd-devil">Pithos</DropdownItem>
                    <DropdownItem href="#" icon="ion-ios-monitor">BSOD Enabler</DropdownItem>
                    <DropdownItem href="#" icon="ion-chatbox-working">Hipchat Emoticons for All</DropdownItem>
                    <DropdownItem href="#" icon="ion-social-windows">Custom PC</DropdownItem>
                    <DropdownItem href="#" icon="ion-android-more-vertical">More Projects...</DropdownItem>
                  </Dropdown>
                  <li className="dropdown">
                    <a className="dropdown-toggle"
                      data-toggle="dropdown"
                      role="button"
                      aria-haspopup="true"
                      aria-expanded="false">
                      Code <i className="icon ion-ios-arrow-up navbar-icon h4"></i>
                    </a>
                    <ul className="dropdown-menu dropup">
                      <li><a href="#"><i className="icon ion-code-working"></i> Code Challenges</a></li>
                      <li><a href=""><i className="icon ion-ios-circle-filled"></i> Morse Code Decoder</a></li>
                      <li><a href=""><i className="icon ion-ios-game-controller-a"></i> The Wiki Game Solver</a></li>
                    </ul>
                  </li>
                  <NavItem href="#">Link 1</NavItem>
                </ul>
              </div>
            </div>
          </nav>
        </div>
      </span>
    );
  }
}
