from project.common.views import CustomTemplate
from .utils import get_post
from django.http import Http404


class BlogView(CustomTemplate):
    template_name="blog/posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = self.blog_data
        return context

    def dispatch(self, request, *args, **kwargs):
        self.blog_data = get_post(kwargs['slug'])
        if not self.blog_data:
            raise Http404
        self.html_title = self.blog_data['title']
        return super().dispatch(request, *args, **kwargs)
