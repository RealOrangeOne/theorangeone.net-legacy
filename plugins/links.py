from collections import namedtuple
from random import shuffle
from config import settings, DotDictionary


ProjectLink = namedtuple("ProjectLink", ["name", "url", "image"])


def accounts():
    links = {}
    for key, (site, user, url, icon) in settings.accounts.items():
        links[key] = DotDictionary({
            'site': site,
            'username': user,
            'url': url.format(user),
            'icon': icon
        })
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
