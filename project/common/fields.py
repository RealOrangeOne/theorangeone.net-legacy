from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks


def build_header_fields():
    for i in range(6):
        h_tag = "h" + str(i + 1)
        yield (h_tag, blocks.CharBlock(classname=h_tag, label=h_tag.upper(), icon="title"))


def build_fixed_fields():
    return [
        ('list', blocks.ListBlock(blocks.CharBlock(label="List Item"), label="list-ul")),
        ('paragraph', blocks.RichTextBlock()),
        ('raw_html', blocks.RawHTMLBlock(label="Raw HTML")),
        ('secret', blocks.RichTextBlock(icon="password", template='blocks/secret.html')),
    ]


def build_stream_field():
    fields = []
    for field_builder in [
        build_header_fields,
        build_fixed_fields
    ]:
        for field in field_builder():
            fields.append(field)
    return StreamField(fields)
