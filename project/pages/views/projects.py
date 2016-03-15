from project.common.views import CustomTemplate, MarkdownView
from json import load
from django.conf import settings
import os.path


PROJECT_DETAILS = load(open(os.path.join(settings.BASE_DIR, 'data/projects.json')))


class AllView(CustomTemplate):
    template_name = 'projects/all.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = PROJECT_DETAILS
        return context


class ProjectView(MarkdownView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            details = PROJECT_DETAILS[kwargs['project']]
            context['html_title'] = details.title
            context['page_title'] = details.title
            context['header_image'] = details.image
        except:
            context['html_title'] = kwargs['project']
            context['page_title'] = kwargs['project']
        return context

    def dispatch(self, request, *args, **kwargs):
        self.markdown = 'projects/{0}.md'.format(kwargs['project'])
        return super().dispatch(request, *args, **kwargs)
