from wagtail.wagtailcore.models import Page
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin


class Entity(MetadataPageMixin, Page):
    is_home = False

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    post_date = models.DateTimeField(null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.SET_NULL
    )

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('post_date'),
            FieldPanel('search_description'),
            ImageChooserPanel('image'),
        ], 'Common page configuration'),
    ]

    @property
    def short_body(self):
        body_words = str(self.body).split(' ')
        return ' '.join(body_words[:30])  # limit to 30 words (ish)

    def get_meta_image(self):
        return self.image

    def get_meta_description(self):
        return self.search_description or self.short_body

    class Meta:
        abstract = True
