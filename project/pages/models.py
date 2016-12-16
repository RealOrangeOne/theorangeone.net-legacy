from django.db import models
from project.common.blocks import build_stream_field
from project.common.models import Entity
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel


class SimpleContentPage(Entity):
    body = build_stream_field()

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]


class SectionIndexPage(Entity):
    body = RichTextField(blank=True)
    hide_list = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('hide_list')
    ]
