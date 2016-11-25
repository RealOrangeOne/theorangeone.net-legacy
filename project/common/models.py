from django.db import models
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class Entity(Page):
    is_home = False

    class Meta:
        abstract = True


class SectionIndexPage(Entity):
    name = models.CharField(max_length=250)
    intro = RichTextField(blank=True)
    hide_list = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('intro', classname="full"),
        FieldPanel('hide_list')
    ]
