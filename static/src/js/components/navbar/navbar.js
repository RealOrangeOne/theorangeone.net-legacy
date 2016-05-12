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
                <ul className="nav navbar-nav home-button hidden-sm hidden-md">
                  <Item href="/" icon="ion-home" />
                </ul>
                <ul className="nav navbar-nav" id="navigation">
                  <Dropdown title="Projects">
                    <Item href="/projects/yoga-pal/" icon="ion-laptop">Yoga Pal</Item>
                    <Item href="/projects/bsod-enabler/" icon="ion-ios-monitor">BSOD Enabler</Item>
                    <Item href="/projects/hipchat-emoticons-for-all/" icon="ion-chatbox-working">
                        Hipchat Emoticons for All
                    </Item>
                    <Item href="#" icon="ion-social-windows">Custom PC</Item>
                    <Item href="/projects/" icon="ion-android-more-vertical">All Projects...</Item>
                  </Dropdown>
                  <Dropdown title="Code">
                    <Item href="#" icon="ion-code-working">Code Challenges</Item>
                    <Item href="#" icon="ion-ios-circle-filled">Pi Time Lapse</Item>
                  <Item href="/projects/wiki-game-solver/" icon="ion-ios-game-controller-a">The Wiki Game Solver</Item>
                  </Dropdown>
                  <Dropdown title="College">
                    <Item href="/robotics/">Student Robotics</Item>
                    <Item href="/college/attack-on-blocks/" icon="ion-cube">Attack on Blocks Game</Item>
                    <Item href="/college/student-server/" icon="glyphicon-hdd">Student Server</Item>
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
                    <Item href="/blog/" icon="ion-social-rss">Blog</Item>
                    <Item href="https://www.flickr.com/photos/theorangeone/" icon="ion-social-camera">Gallery</Item>
                  </Dropdown>
                  <Item href="#">Links</Item>
                  <Dropdown title="About">
                    <Item href="/about/me/" icon="ion-android-person">Me</Item>
                    <Item href="/about/website/" icon="ion-cloud">Website</Item>
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
