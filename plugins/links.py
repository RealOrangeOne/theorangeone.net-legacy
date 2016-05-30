from collections import namedtuple
from random import shuffle


SocialLink = namedtuple("SocialLink", ["name", "url", "icon"])
ProjectLink = namedtuple("ProjectLink", ["name", "url", "image"])


def social():
    return {
        "github": SocialLink("GitHub", "https://github.com/RealOrangeOne", "fa-github"),
        "twitter": SocialLink("Twitter", "https://twitter.com/RealOrangeOne", "fa-twitter"),
        "reddit": SocialLink("Reddit", "https://reddit.com/user/RealOrangeOne", "fa-reddit"),
        "instagram": SocialLink("Instagram", "https://instagram.com/RealOrangeOne", "fa-instagram"),
        "youtube": SocialLink("YouTube", "https://youtube.com/user/TheOrangeOneOfficial", "fa-youtube"),
        "flickr": SocialLink("Flickr", "https://www.flickr.com/photos/theorangeone/", "fa-flickr")
    }


def index_projects():
    projects = [
        ProjectLink("Student Robotics", "/robotics/", "https://c2.staticflickr.com/8/7711/17122633430_e1b599fe47.jpg"),
        ProjectLink("Dotfiles", "/projects/dotfiles/", "http://jleajones.com/assets/images/dotfiles.png"),
        ProjectLink("Custom PC", "/setup/custom-pc/", "https://c2.staticflickr.com/8/7083/27071954860_f6096ccce6.jpg")
    ]
    shuffle(projects)
    return projects
