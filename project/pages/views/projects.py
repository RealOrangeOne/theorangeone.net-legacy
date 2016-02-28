from collections import namedtuple
from project.common.views import CustomTemplate, MarkdownView


ProjectDetails = namedtuple('ProjectDetails', ['title', 'image'])

PROJECT_DETAILS = {
    'hipchat-emoticons-for-all': ProjectDetails('Hipchat Emoticons Plugin', 'https://hipchat-magnolia-cdn.atlassian.com/assets/img/hipchat/hipchat_og_image.jpg'),
    'attack-on-blocks': ProjectDetails('Attack on Blocks Game', 'https://image.freepik.com/free-vector/space-invaders-game_62147502273.jpg')
}


class AllView(CustomTemplate):
    template_name = 'projects/all.html'


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
