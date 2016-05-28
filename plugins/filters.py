import iso8601
from bs4 import BeautifulSoup


def format_datetime(value):
    return iso8601.parse_date(str(value)).strftime("%x %-H:%M")


def html_to_raw(html):
    soup = BeautifulSoup(html, "html.parser")
    for script in soup(["script", "style"]):  # Remove script / style tags
        script.extract()
    return soup.get_text()


def category_find(categories, name):
    for category_name, articles in categories:
        if category_name == name:
            return articles
    return []
