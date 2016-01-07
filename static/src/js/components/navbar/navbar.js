import React from 'react';
import Header from './header';
import Dropdown from './dropdown';
import Item from './item';

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
                    <Item href="#" icon="ion-social-freebsd-devil">Pithos</Item>
                    <Item href="#" icon="ion-ios-monitor">BSOD Enabler</Item>
                    <Item href="#" icon="ion-chatbox-working">Hipchat Emoticons for All</Item>
                    <Item href="#" icon="ion-social-windows">Custom PC</Item>
                    <Item href="#" icon="ion-android-more-vertical">All Projects...</Item>
                  </Dropdown>
                  <Dropdown title="Code">
                    <Item href="#" icon="ion-code-working">Code Challenges</Item>
                    <Item href="#" icon="ion-ios-circle-filled">BSOD Enabler</Item>
                    <Item href="#" icon="ion-ios-game-controller-a">The Wiki Game Solver</Item>
                  </Dropdown>
                  <Item href="#">Link 1</Item>
                </ul>
              </div>
            </div>
          </nav>
        </div>
      </span>
    );
  }
}
