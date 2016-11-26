from django.db import models
from django.core.exceptions import ValidationError

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from project.common.models import Entity


ALLOWED_DOMAINS = [
    'github'
]


def validate_url(value):
    for part in ALLOWED_DOMAINS:
        if part in value.lower():
            return True
    raise ValidationError('Invalid domain, should be in {}'.format(ALLOWED_DOMAINS))


class ProjectPage(Entity):
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField()
    url = models.URLField(validators=[validate_url], blank=True)
    download_url = models.URLField(validators=[validate_url], blank=True)
    asset = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_download_url(self):
        return self.download_url or self.asset.url

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('main_image'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('url'),
        FieldPanel('download_url'),
        DocumentChooserPanel('asset')
    ]
