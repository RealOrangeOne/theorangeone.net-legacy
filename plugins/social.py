from collections import namedtuple


SocialLink = namedtuple('SocialLink', ['name', 'url', 'icon'])


def generate():
    return {
        "github": SocialLink("GitHub", "https://github.com/RealOrangeOne", "fa-github"),
        "twitter": SocialLink("Twitter", "https://twitter.com/RealOrangeOne", "fa-twitter"),
        "reddit": SocialLink("Reddit", "https://reddit.com/user/RealOrangeOne", "fa-reddit"),
        "instagram": SocialLink("Instagram", "https://instagram.com/RealOrangeOne", "fa-instagram"),
        "youtube": SocialLink("YouTube", "https://youtube.com/user/TheOrangeOneOfficial", "fa-youtube")
    }
