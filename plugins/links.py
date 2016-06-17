from collections import namedtuple
from random import shuffle

ProjectLink = namedtuple("ProjectLink", ["name", "url", "image"])
Account = namedtuple("Account", ["name", "url", "icon", "username"])


def accounts():
    links = {
        "github": Account("GitHub", "https://github.com/RealOrangeOne/", "fa-github", "RealOrangeOne"),
        "twitter": Account("Twitter", "https://twitter.com/RealOrangeOne", "fa-twitter", "@RealOrangeOne"),
        "reddit": Account("Reddit", "https://reddit.com/user/RealOrangeOne", "fa-reddit", "/u/RealOrangeOne"),
        "instagram": Account("Instagram", "https://instagram.com/RealOrangeOne", "fa-instagram", "RealOrangeOne"),
        "youtube": Account("YouTube", "https://youtube.com/user/TheOrangeOneOfficial", "fa-youtube", "TheOrangeOneOfficial"),
        "flickr": Account("Flickr", "https://flickr.com/photos/TheOrangeOne/", "fa-flickr", "TheOrangeOne"),
    }
    return links


def footer():
    footer_accounts = ["github", "twitter", "reddit", "instagram", "youtube", "flickr"]
    all_accounts = accounts()
    footer_links = []
    for account in footer_accounts:
        footer_links.append(all_accounts[account])
    return footer_links


def index_projects():
    projects = [
        ProjectLink("Student Robotics", "/robotics/", "https://c2.staticflickr.com/8/7711/17122633430_e1b599fe47.jpg"),
        ProjectLink("Dotfiles", "/projects/dotfiles/", "http://jleajones.com/assets/images/dotfiles.png"),
        ProjectLink("Custom PC", "/setup/custom-pc/", "https://c2.staticflickr.com/8/7083/27071954860_f6096ccce6.jpg")
    ]
    shuffle(projects)
    return projects
