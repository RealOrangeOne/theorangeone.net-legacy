from django.views.generic import TemplateView
from .utils import get_post, reformat_date
from django.http import Http404


class BlogView(TemplateView):
    template_name = "blog/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = self.blog_data
        context['blog']['date'] = reformat_date(self.blog_data['date'])
        context['html_title'] = self.blog_data['title']
        return context

    def dispatch(self, request, *args, **kwargs):
        self.blog_data = get_post(kwargs['slug'])
        if not self.blog_data:
            raise Http404
        return super().dispatch(request, *args, **kwargs)
