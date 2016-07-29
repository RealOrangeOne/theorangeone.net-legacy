from pelican import signals
from .links import accounts
import os.path


ACCOUNTS = accounts()


def map_og_tag(instance, prop, og_tag, default=''):
    data = instance.metadata.get(prop, default)
    if data:
        instance.ogtags.append((og_tag, data))
    return instance


def get_content_type(instance):
    return type(instance).__name__

def get_twiter_tags(instance):
    return {
        "twitter:card": "summary_large_image",
        "twitter:site": ACCOUNTS["twitter"].username,
        "twitter:title": instance.metadata.get("title"),
        "twitter:description": instance.metadata.get("summary"),
        "twitter:creator": ACCOUNTS["twitter"].username,
        "twitter:image": instance.metadata.get('image'),
        "twitter:image:alt": instance.metadata.get("summary"),
        "twitter:url": os.path.join(instance.settings.get("SITEURL", ""), instance.url)
    }

def get_og_tags(instance):
    return {
        "og:title": instance.metadata.get("title"),
        "og:type": get_content_type(instance).lower(),
        "og:url": os.path.join(instance.settings.get("SITEURL"), instance.url),
        "og:image": instance.metadata.get("image"),
        "og:description": instance.metadata.get("description"),
        "og:site_name": instance.settings.get("SITENAME"),
        "og:locale": instance.metadata.get("locale", "en_GB")
    }

def get_schema_tags(instance):
    return {
        "name": instance.metadata.get("title"),
        "description": instance.metadata.get("description"),
        "image": instance.metadata.get("image")
    }

def get_general_tags(instance):
    return {
        "article:author": instance.settings.get("AUTHOR"),
        "article:modified_time": instance.metadata.get("modified"),
        "article:published_time": instance.metadata.get("date"),
        "article:section": instance.category.name if hasattr(instance, "category") else ""
        "description": instance.metadata.get("description"),
        "author": instance.metadata.get("author", instance.settings.get("AUTHOR")),
        "canonical": instance.gettings.get("SITEURL")
    }

def tag_item(instance):
    instance_type = get_content_type(instance)

    if instance_type not in ['Article', 'Page', 'Draft']:
        return

    metatags = []

    for tag, value in get_twiter_tags(instance).items():
        metatags.append(
            "<meta name='{0}' content='{1}' />".format(tag, value)
        )

    for tag, value in get_og_tags(instance).items():
        metatags.append(
            "<meta property='{0}' content='{1}' />".format(tag, value)
        )

    for tag, value in get_schema_tags(instance).items():
        metatags.append(
            "<meta itemprop='{0}' content='{1}' />".format(tag, value)
        )

    general_tags = get_general_tags(instance).items()
    if hasattr(instance, 'tags'):
        for tag in instance.tags:
            general_tags.append(('article:tag', tag.name))

    for tag, value in general_tags:
        metatags.append(
            "<meta name='{0}' content='{1}' />".format(tag, value)
        )

    instance.metatags = metatags


def register():
    signals.content_object_init.connect(tag_item)
