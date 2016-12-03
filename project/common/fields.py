from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock


def build_header_fields():
    for i in range(6):
        h_tag = "h" + str(i + 1)
        yield (h_tag, blocks.CharBlock(classname=h_tag, label=h_tag.upper(), icon="title"))


def build_fixed_fields():
    return [
        ('ansi', blocks.TextBlock(template="blocks/ansi.html")),
        ('document', DocumentChooserBlock()),
        ('gist', blocks.CharBlock(template="blocks/gist.html")),
        ('image', ImageChooserBlock()),
        ('ol', blocks.ListBlock(blocks.CharBlock(label="List Item"), label="Ordered List", template='blocks/ordered-list.html')),
        ('paragraph', blocks.RichTextBlock()),
        ('raw_html', blocks.RawHTMLBlock(label="Raw HTML")),
        ('secret', blocks.RichTextBlock(icon="password", template='blocks/secret.html')),
        ('ul', blocks.ListBlock(blocks.CharBlock(label="List Item"), label="Unordered List")),
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
