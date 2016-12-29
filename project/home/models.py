from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from project.blog.models import BlogPage
from project.common.models import Entity


class HomePage(Entity):
    is_home = True

    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['blog_posts'] = BlogPage.objects.live().order_by('-post_date')[:4]
        return context
