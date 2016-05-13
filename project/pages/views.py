import os.path
from django.conf import settings
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from .utils import get_context, parse_content, get_title_from_markdown, swap_page


def page_view(request, path):
    template = None
    if path.endswith('/'):  # Strip trailing slash
        path = path[:-1]

    path = swap_page(path)

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
        context['html_title'] = context['page_title']
        parsed_content = template.render(context, request)
    return HttpResponse(parsed_content)
