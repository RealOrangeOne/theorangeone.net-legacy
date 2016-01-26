from project.common.views import CustomTemplate, MarkdownView


class AllView(CustomTemplate):
    template_name = 'projects/all.html'


class ProjectView(MarkdownView):
    def dispatch(self, request, *args, **kwargs):
        self.markdown = 'projects/{0}.md'.format(kwargs['project'])
        return super().dispatch(request, *args, **kwargs)
