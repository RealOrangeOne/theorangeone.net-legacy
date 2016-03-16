from project.common.views import CustomTemplate
from django.conf import settings
from json import load
import os.path


class IndexView(CustomTemplate):
    template_name = 'index.html'
    html_title = "Homepage"
    body_class = "index"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = load(open(os.path.join(settings.BASE_DIR, 'data/projects.json')))
        return context


class NoJavascriptView(CustomTemplate):
    template_name = 'core/no-js.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['js_redirect'] = False
        return context


class Custom404View(CustomTemplate):
    template_name = 'core/404.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)
