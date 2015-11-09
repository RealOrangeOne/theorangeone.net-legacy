from django.views.generic import TemplateView
from project.common.views import CustomHeaderBG
from django.contrib.staticfiles.templatetags.staticfiles import static


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['body_class'] = "index"
        return context



class NoJavascriptView(TemplateView):
    template_name = 'core/no-js.html'


class Custom404View(CustomHeaderBG.Template):
    template_name = 'core/404.html'
    header_BG = static('img/ninjas.png')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['no_footer'] = True
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)


class AboutWebsiteView(CustomHeaderBG.Template):
    template_name = 'about/website.html'
    header_BG = ''


class AboutIndexView(TemplateView):
    template_name = 'about/index.html'