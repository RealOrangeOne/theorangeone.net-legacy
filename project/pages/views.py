from django.views.generic import TemplateView
from project.common.views import CustomHeaderBG
from django.contrib.staticfiles.templatetags.staticfiles import static


class IndexView(TemplateView):
    template_name = 'index.html'


class NoJavascriptView(TemplateView):
    template_name = 'core/no-js.html'


class Custom404View(CustomHeaderBG.Template):
    template_name = 'core/404.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)


class AboutWebsiteView(CustomHeaderBG.Template):
    template_name = 'about/website.html'


class AboutIndexView(TemplateView):
    template_name = 'about/index.html'
