from pelican import signals
import os.path


def screenfetch(instance):
    base_path = os.path.dirname(os.path.abspath(__file__))
    if type(instance).__name__ not in ['Article', 'Page', 'Draft']:
        return

    if not instance.metadata.get('screenfetch_path', False):
        return

    content_dir = os.path.join(base_path, instance.settings['PATH'])

    file_data = open(os.path.join(content_dir, instance.metadata['screenfetch_path'])).read()
    instance.screenfetch = "<pre class='highlight ansi-up'>{0}</pre>".format(file_data)


def register():
    signals.content_object_init.connect(screenfetch)
