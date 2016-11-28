from django.db import models
from project.common.models import Entity
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class SimpleContentPage(Entity):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

class SectionIndexPage(Entity):
    intro = RichTextField(blank=True)
    hide_list = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('hide_list')
    ]
