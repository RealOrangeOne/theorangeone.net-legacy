from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtailmarkdown.blocks import MarkdownBlock
from wagtail.wagtailembeds.blocks import EmbedBlock


HEADING_CHOICES = [('h' + str(i), 'H' + str(i)) for i in range(1, 6)]


class HeadingBlock(blocks.StructBlock):
    size = blocks.ChoiceBlock(choices=HEADING_CHOICES)
    value = blocks.CharBlock()

    class Meta:
        icon = 'title'
        template = 'blocks/heading.html'


class VideoBlock(blocks.StructBlock):
    video = EmbedBlock()
    caption = blocks.CharBlock()

    class Meta:
        template = 'blocks/video.html'


def build_stream_field():
    return StreamField([
        ('ansi', blocks.TextBlock(template="blocks/ansi.html")),
        ('document', DocumentChooserBlock()),
        ('gist', blocks.CharBlock(icon="code", template="blocks/gist.html")),
        ('heading', HeadingBlock()),
        ('image', ImageChooserBlock()),
        ('markdown', MarkdownBlock()),
        ('ol', blocks.ListBlock(blocks.CharBlock(label="List Item"), icon="list-ol", label="Ordered List", template='blocks/ordered-list.html')),
        ('paragraph', blocks.RichTextBlock()),
        ('raw_html', blocks.RawHTMLBlock(label="Raw HTML")),
        ('secret', blocks.RichTextBlock(icon="password", template='blocks/secret.html')),
        ('ul', blocks.ListBlock(blocks.CharBlock(label="List Item"), icon="list-ul", label="Unordered List")),
        ('video', VideoBlock())
    ])
