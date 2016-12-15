from django.db import models
from django.core.exceptions import ValidationError
from project.common.blocks import build_stream_field
from wagtail.wagtailcore.models import Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
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
    summary = models.CharField(max_length=500)
    body = build_stream_field()
    project_url = models.URLField(validators=[validate_url], blank=True)
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
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
        FieldPanel('summary'),
        StreamFieldPanel('body'),
        FieldPanel('download_url'),
        FieldPanel('project_url'),
        DocumentChooserPanel('asset')
    ]
