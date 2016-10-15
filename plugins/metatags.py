from bs4 import BeautifulSoup
from pelican import signals
import os.path


def get_content_type(instance):
    return type(instance).__name__


def html_to_raw(html):
    parsed = BeautifulSoup(html, "html.parser")
    for script in parsed(["script", "style"]):  # Remove extra tags
        script.extract()
    return parsed.get_text()


def get_twiter_tags(instance):
    return {
        "twitter:card": "summary_large_image",
        "twitter:site": instance.settings.get("ACCOUNTS")["twitter"].username,
        "twitter:title": instance.metadata.get("title", ""),
        "twitter:description": html_to_raw(instance.metadata.get("summary", "")),
        "twitter:creator": instance.settings.get("ACCOUNTS")["twitter"].username,
        "twitter:image": instance.metadata.get("image", ""),
        "twitter:image:alt": html_to_raw(instance.metadata.get("summary", "")),
        "twitter:url": os.path.join(instance.settings.get("SITEURL", ""), instance.url)
    }


def get_og_tags(instance):
    return {
        "og:title": instance.metadata.get("title", ""),
        "og:type": get_content_type(instance).lower(),
        "og:url": os.path.join(instance.settings.get("SITEURL"), instance.url),
        "og:image": instance.metadata.get("image", ""),
        "og:description": html_to_raw(instance.metadata.get("summary", "")),
        "og:site_name": instance.settings.get("SITENAME"),
        "og:locale": instance.metadata.get("locale", "en_GB")
    }


def get_schema_tags(instance):
    return {
        "name": instance.metadata.get("title", ""),
        "description": html_to_raw(instance.metadata.get("summary", "")),
        "image": instance.metadata.get("image", "")
    }


def get_general_tags(instance):
    return {
        "article:author": instance.settings.get("AUTHOR"),
        "article:modified_time": instance.metadata.get("modified", ""),  # Set build time as default?
        "article:published_time": instance.metadata.get("date", ""),
        "article:section": instance.category.name if hasattr(instance, "category") else "",
        "description": html_to_raw(instance.metadata.get("summary", "")),
        "author": instance.metadata.get("author", instance.settings.get("AUTHOR")),
        "canonical": instance.settings.get("SITEURL")
    }


def tag_item(instance):
    instance_type = get_content_type(instance)

    if instance_type not in ['Article', 'Page', 'Draft']:
        return

    metatags = []

    for tag, value in get_twiter_tags(instance).items():
        if not value:
            continue
        metatags.append(
            "<meta name=\"{0}\" content=\"{1}\" />".format(tag, value)
        )

    for tag, value in get_og_tags(instance).items():
        if not value:
            continue
        metatags.append(
            "<meta property=\"{0}\" content=\"{1}\" />".format(tag, value)
        )

    for tag, value in get_schema_tags(instance).items():
        if not value:
            continue
        metatags.append(
            "<meta itemprop=\"{0}\" content=\"{1}\" />".format(tag, value)
        )

    general_tags = get_general_tags(instance).items()
    if hasattr(instance, 'tags'):
        for tag in instance.tags:
            general_tags.append(('article:tag', tag.name))

    for tag, value in general_tags:
        if not value:
            continue
        metatags.append(
            "<meta name=\"{0}\" content=\"{1}\" />".format(tag, value)
        )

    instance.metatags = '\n'.join(metatags)


def register():
    signals.content_object_init.connect(tag_item)
