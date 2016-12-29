from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from project.blog.models import BlogPage
from project.projects.models import ProjectPage
from project.common.models import Entity
from project.common.utils import round_to_multiple


class HomePage(Entity):
    is_home = True

    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full")
    ]

    def get_context(self, *args, **kwargs):
        context = super().get_context(*args, **kwargs)
        context['blog_posts'] = BlogPage.objects.live().order_by('-post_date')[:4]
        projects = ProjectPage.objects.live().filter(search_image__isnull=False)
        projects_to_show = round_to_multiple(projects.count(), 3) if projects.count() >= 3 else projects.count()
        context['projects'] = projects[:projects_to_show]
        return context
