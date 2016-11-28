from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks


def build_stream_field():
    return StreamField([
        ('h1', blocks.CharBlock(classname="h1", label="H1")),
        ('h2', blocks.CharBlock(classname="h2", label="H2")),
        ('paragraph', blocks.RichTextBlock()),
        ('raw_html', blocks.RawHTMLBlock(label="Raw HTML")),
        ('list', blocks.ListBlock(blocks.CharBlock(label="List Item")))
    ])
