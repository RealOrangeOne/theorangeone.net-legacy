import iso8601


def get_attribute(cls, attr, default=None):
    return getattr(cls, attr, default)


def format_datetime(value):
    return iso8601.parse_date(str(value)).strftime("%x")


def category_find(categories, name):
    for category_name, articles in categories:
        if category_name == name:
            return articles
    return []


def limit(line, length):
    if isinstance(line, str):
        if len(line) <= length:
            return line
        return " ".join(line.split(" ")[:length]) + '...'
    elif isinstance(line, list):
        return line[:length]


def get_title(instance):
    return (
        get_attribute(instance, 'title') or (hasattr(instance, 'page') and get_attribute(instance.page, 'name')) or get_attribute(instance, 'name') or ''
    )


def get_html_title(instance):
    return (
        get_attribute(instance, 'html_title') or get_title(instance)
    )


def get_image(instance):
    return get_attribute(instance, 'image') or (hasattr(instance, 'page') and get_attribute(instance.page, 'name')) or ''
