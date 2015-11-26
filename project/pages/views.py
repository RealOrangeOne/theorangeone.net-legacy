from project.common.views import CustomTemplate


class IndexView(CustomTemplate):
    template_name = 'index.html'
    html_title = "Homepage"
    body_class = "index"


class NoJavascriptView(CustomTemplate):
    template_name = 'core/no-js.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['no_js_redirect'] = True
        return context


class Custom404View(CustomTemplate):
    template_name = 'core/404.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)


class AboutWebsiteView(CustomTemplate):
    template_name = 'about/website.html'


class AboutIndexView(CustomTemplate):
    template_name = 'about/index.html'
