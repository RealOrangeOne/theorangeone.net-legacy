from django.conf import settings
from bs4 import BeautifulSoup
import markdown2


def get_context(path):
    if path in settings.PAGE_CONTEXT:
        context = dict(settings.DEFAULT_CONTEXT, **settings.PAGE_CONTEXT[path])
    else:
        context = dict(settings.DEFAULT_CONTEXT)
    return context


def get_title_from_markdown(md):
    html_tree = BeautifulSoup(md, "html.parser")
    tag = html_tree.find('h1')
    return tag.contents[0]


def parse_content(content, extension):
    if extension == 'md':
        return markdown2.markdown(content)
    return content
