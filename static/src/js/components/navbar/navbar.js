import React from 'react';
import Header from './header';
import Dropdown from './dropdown';
import Item from './item';

export default class NavBar extends React.Component {
  render() {
    return (
      <span>
        <div id="navbar-anchor" />
        <div id="navbar-container" className="align">
          <nav className="navbar navbar-inverse">
            <div className="container-fluid">
              <Header />
              <div className="collapse navbar-collapse" id="navbar">
                <ul className="nav navbar-nav home-button hidden-sm">
                  <Item href="/" icon="ion-home" />
                </ul>
                <ul className="nav navbar-nav" id="navigation">
                  <Dropdown title="Projects">
                    <Item ident="pages:projects" args={['pithos']} icon="ion-social-freebsd-devil">Pithos</Item>
                    <Item href="#" icon="ion-ios-monitor">BSOD Enabler</Item>
                    <Item href="#" icon="ion-chatbox-working">Hipchat Emoticons for All</Item>
                    <Item href="#" icon="ion-social-windows">Custom PC</Item>
                    <Item ident="pages:all-projects" icon="ion-android-more-vertical">All Projects...</Item>
                  </Dropdown>
                  <Dropdown title="Code">
                    <Item href="#" icon="ion-code-working">Code Challenges</Item>
                    <Item href="#" icon="ion-ios-circle-filled">BSOD Enabler</Item>
                    <Item href="#" icon="ion-ios-game-controller-a">The Wiki Game Solver</Item>
                  </Dropdown>
                  <Dropdown title="College">
                    <Item href="#">Student Robotics</Item>
                    <Item href="#" icon="ion-cube">Attack on Blocks Game</Item>
                    <Item href="#">Student Server</Item>
                    <Item href="#" icon="ion-ios-paper">EPQ</Item>
                    <Item href="#">Wall of Sheep</Item>
                  </Dropdown>
                  <Dropdown title="Setup">
                    <Item href="#">&#128129; Desk</Item>
                    <Item href="#" icon="ion-briefcase">Work</Item>
                    <Item href="#" icon="ion-model-s">On The Go</Item>
                    <Item href="#" icon="ion-android-phone-portrait">Devices</Item>
                    <Item href="#">Servers</Item>
                  </Dropdown>
                  <Dropdown title="Work">
                    <Item href="#" icon="ion-form-repo">Projects</Item>
                    <Item href="#" icon="ion-android-desktop">Setup</Item>
                  </Dropdown>
                  <Dropdown title="Media">
                    <Item
                      href="https://www.youtube.com/user/TheOrangeOneOfficial"
                      icon="ion-social-youtube">
                      YouTube Channel
                    </Item>
                    <Item href="#" icon="ion-social-rss">Feed</Item>
                    <Item href="https://www.flickr.com/photos/theorangeone/" icon="ion-social-camera">Gallery</Item>
                  </Dropdown>
                  <Item href="#">Links</Item>
                  <Dropdown title="About">
                    <Item ident="pages:about-me" icon="ion-android-person">Me</Item>
                  <Item ident="pages:about-website" icon="">Website</Item>
                    <Item href="#" icon="ion-android-contacts">Contact Me</Item>
                  </Dropdown>
                </ul>
              </div>
            </div>
          </nav>
        </div>
      </span>
    );
  }
}
