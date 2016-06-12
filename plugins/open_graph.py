import os.path

from pelican import signals


def map_og_tag(instance, prop, og_tag, default=''):
    data = instance.metadata.get(prop, default)
    if data:
        instance.ogtags.append((og_tag, data))
    return instance


def get_content_type(instance):
    return type(instance).__name__


def tag_item(instance):
    instance_type = get_content_type(instance)

    if instance_type not in ['Article', 'Page', 'Draft']:
        return

    instance.ogtags = [
        ('og:type', instance_type),
        ('og:url', os.path.join(instance.settings.get('SITEURL', ''), instance.url)),
        ('twitter:url', os.path.join(instance.settings.get('SITEURL', ''), instance.url)),
        ('twitter:card', 'summary'),
        ('og:site_name', instance.settings.get('SITENAME', '')),
    ]

    instance = map_og_tag(instance, 'title', 'og:title')
    instance = map_og_tag(instance, 'image', 'og:image')
    instance = map_og_tag(instance, 'summary', 'og:description')
    instance = map_og_tag(instance, 'author', 'article:author', instance.settings.get('AUTHOR'))
    instance = map_og_tag(instance, 'modified', 'article:modified_time')
    instance = map_og_tag(instance, 'date', 'article:published_time')

    instance = map_og_tag(instance, 'image', 'twitter:image')
    instance = map_og_tag(instance, 'title', 'twitter:title')
    instance = map_og_tag(instance, 'summary', 'twitter:description')

    if hasattr(instance, 'category'):
        instance.ogtags.append(('article:section', instance.category.name))

    if hasattr(instance, 'tags'):
        for tag in instance.tags:
            instance.ogtags.append(('article:tag', tag.name))

    instance.ogtags.append(('og:locale', instance.metadata.get('locale', 'en_GB')))

    # Add non-og tags
    instance = map_og_tag(instance, 'summary', 'description')
    instance = map_og_tag(instance, 'author', 'author', instance.settings.get('AUTHOR'))
    instance.ogtags.append(('canonical', instance.settings.get('SITEURL')))


def register():
    signals.content_object_init.connect(tag_item)
