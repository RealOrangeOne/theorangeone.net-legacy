from django.views.generic import TemplateView


class CustomTemplate(TemplateView):
    html_title = ""
    body_class = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['html_title'] = self.html_title
        context['body_class'] = self.body_class
        return context
