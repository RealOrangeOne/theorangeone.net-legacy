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
        "bitbucket": Account("BitBucket", "https://bitbucket.org/TheOrangeOne", "fa-bitbucket", "TheOrangeOne"),
        "trello": Account("Trello", "https://trello.com/TheOrangeOne", "fa-trello", "TheOrangeOne"),
        "freenode": Account("Freenode", "https://webchat.freenode.net", "fa-rss", "TheOrangeOne"),
        "atomio": Account("Atomio Slack", "https://atomio.slack.com", "fa-slack", "TheOrangeOne"),
        "pcpartpicker": Account("PCPartPicker", "https://uk.pcpartpicker.com/user/theorangeone97", "fa-desktop", "TheOrangeOne97"),
        "codepen": Account("CodePen", "https://codepen.io/TheOrangeOne", "fa-codepen", "TheOrangeOne"),
        "npm": Account("npm", "https://www.npmjs.com/~TheOrangeOne", "fa-file-code-io", "TheOrangeOne")
    }
    return links


def footer():
    footer_accounts = ["github", "twitter", "reddit", "instagram", "youtube", "flickr"]
    all_accounts = accounts()
    return [all_accounts[account] for account in footer_accounts]


def index_projects():
    projects = [
        ProjectLink("Student Robotics", "/robotics/", "https://c2.staticflickr.com/8/7711/17122633430_e1b599fe47.jpg"),
        ProjectLink("Dotfiles", "/projects/dotfiles/", "http://jleajones.com/assets/images/dotfiles.png"),
        ProjectLink("Custom PC", "/setup/custom-pc/", "https://c2.staticflickr.com/8/7083/27071954860_f6096ccce6.jpg"),
        ProjectLink("Yoga-Pal", "/projects/yoga-pal/", "http://brain-images.cdn.dixons.com/8/1/10135218/l_10135218_002.jpg"),
        ProjectLink("React-Native Mock", "/projects/react-native-mock/", "http://i.imgur.com/ZB8O0DL.jpg"),
        ProjectLink("Wall of Sheep", "/wall-of-sheep/", "http://www.hackerstickers.com/uploaded/thumbnails/db_file_img_3582_475xauto.jpg")
    ]
    shuffle(projects)
    return projects
