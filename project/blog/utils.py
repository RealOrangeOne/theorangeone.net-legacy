import requests
from django.conf import settings

API_PATH = "https://public-api.wordpress.com/rest/v1.1/sites/{0}/posts/slug:{1}"


def build_url(slug):
    if not slug:
        return
    return API_PATH.format(settings.WORDPRESS_URL, slug)


def get_post(slug):
    if not slug:
        return
    response = requests.get(build_url(slug))

    if response.status_code != 200:
        return
    data = response.json()
    return data if "ID" in data else False
