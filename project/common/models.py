from wagtail.wagtailcore.models import Page
from django.db import models
from wagtailmetadata.models import MetadataPageMixin


class Entity(MetadataPageMixin, Page):
    is_home = False

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
