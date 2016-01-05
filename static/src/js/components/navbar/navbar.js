import React from 'react';
import NavBarHeader from './navbar-header';
var NavItem = require('react-bootstrap').NavItem;

export default class NavBar extends React.Component {
  render() {
    return (
      <span>
        <div id="navbar-anchor" />
        <div id="navbar-container" className="align h4">
          <nav className="navbar navbar-inverse">
            <div className="container-fluid">
              <NavBarHeader />
              <div className="collapse navbar-collapse" id="navbar">
                <ul className="nav navbar-nav home-button hidden-sm">
                  <li className="active home"><a href=""><i className="icon ion-home"></i></a></li>
                </ul>
                <ul className="nav navbar-nav" id="navigation">
                  <li className="dropdown">
                    <a className="dropdown-toggle"
                      data-toggle="dropdown"
                      role="button"
                      aria-haspopup="true"
                      aria-expanded="false">
                      Projects <i className="icon ion-ios-arrow-up navbar-icon h4"></i>
                    </a>
                    <ul className="dropdown-menu dropup">
                      <li><a href="#"><i className="icon ion-social-freebsd-devil"></i> Pithos</a></li>
                      <li><a href=""><i className="icon ion-ios-monitor"></i> BSOD Enabler</a></li>
                      <li><a href=""><i className="icon ion-chatbox-working"></i> Hipchat Emoticons for All</a></li>
                      <li><a href=""><i className="icon ion-social-windows"></i> Custom PC</a></li>
                      <li><a href=""><i className="icon ion-android-more-vertical"></i> All Projects...</a></li>
                    </ul>
                  </li>
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
                      <li><a href="">
                        <span className="glyphicon glyphicon-print" aria-hidden="true"></span> Printr
                      </a></li>
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
