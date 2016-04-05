from project.common.views import CustomTemplate
import os.path
from django.conf import settings
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from .utils import get_context, parse_content, get_title_from_markdown


def page_view(request, path):
    template = None
    if os.path.isdir(os.path.join(settings.BASE_DIR, 'templates', path)):
        path = os.path.join(path, 'index')
    for extension in ['md', 'html']:
        try:
            template = get_template("{}.{}".format(path, extension))
            break
        except:
            pass
    if not template:
        raise Http404
    context = get_context(path)
    parsed_content = parse_content(template.render(context, request), extension)
    if extension == 'md':
        template = get_template('markdown_content.html')
        context['markdown_content'] = parsed_content
        context['page_title'] = get_title_from_markdown(parsed_content)
        parsed_content = template.render(context, request)
    return HttpResponse(parsed_content)


def index_view(request):
    return page_view(request, 'index')
