from wagtail.wagtailcore.models import Page


class Entity(Page):
    is_home = False

    class Meta:
        abstract = True


