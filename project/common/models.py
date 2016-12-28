from wagtail.wagtailcore.models import Page
from django.db import models
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtailmetadata.models import MetadataPageMixin
from bs4 import BeautifulSoup
from wagtail.contrib.settings.models import BaseSetting, register_setting


class Entity(MetadataPageMixin, Page):
    is_home = False

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    post_date = models.DateTimeField(null=True, blank=True)

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('post_date'),
            FieldPanel('search_description'),
            ImageChooserPanel('search_image'),
        ], 'Common page configuration'),
    ]

    @property
    def image(self):
        return self.search_image

    @property
    def short_body(self):
        body_words = BeautifulSoup(str(self.body)).get_text().split(' ')
        return ' '.join(body_words[:30]) + '...'  # limit to 30 words (ish)

    def get_meta_description(self):
        return self.search_description or self.short_body

    class Meta:
        abstract = True


@register_setting
class SocialMediaSettings(BaseSetting):
    flickr = models.URLField(help_text="Flickr Profile URL")
    freenode = models.CharField(help_text="Freenode Username", max_length=15)
    github = models.URLField(help_text="GitHub Profile URL")
    reddit = models.URLField(help_text="Reddit Profile URL")
    twitter = models.CharField(help_text='Twitter Username', max_length=15)
    youtube = models.URLField(help_text='Youtube Channel URL')
