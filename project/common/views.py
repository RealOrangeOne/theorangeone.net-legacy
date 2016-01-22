from django.views.generic import TemplateView, FormView
from django.template import loader, Context
from django.template.base import TemplateDoesNotExist
from django.http import Http404
import markdown2

class CustomTemplate(TemplateView):
    html_title = ""
    body_class = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['html_title'] = self.html_title
        context['body_class'] = self.body_class
        context['js_redirect'] = True
        return context


class CustomFormTemplate(FormView):
    html_title = ""
    body_class = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['html_title'] = self.html_title
        context['body_class'] = self.body_class
        context['js_redirect'] = True
        return context


class MarkdownView(CustomTemplate):
    template_name = 'markdown_content.html'
    page_title = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        try:
            markdown_template = loader.get_template(self.markdown)
        except TemplateDoesNotExist:
            raise Http404
        c = Context(self.get_markdown_context().update(context))
        context['markdown_content'] = markdown2.markdown(markdown_template.render(c))
        return context

    def get_markdown_context(self):
        return {}
