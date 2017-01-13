import os
from pelican import signals, contents
from jinja2 import Environment, ChoiceLoader, FileSystemLoader
from config import social

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def execjinja2(instance):
    if type(instance) in (contents.Article, contents.Page):
        jinja2_env = Environment(  # nosec
            loader=ChoiceLoader([
                FileSystemLoader(
                    os.path.join(BASE_DIR, instance.settings['THEME'], 'templates')
                ),
                FileSystemLoader(
                    os.path.join(BASE_DIR, instance.settings['PATH'])
                )
            ]),
            **instance.settings['JINJA_ENVIRONMENT'],
        )

        jinja2_env.filters.update(instance.settings['JINJA_FILTERS'])

        jinja2_template = jinja2_env.from_string(instance._content)

        kwargs = instance._context
        if type(instance) is contents.Article:
            kwargs['article'] = instance
        elif type(instance) is contents.Page:
            kwargs['page'] = instance

        kwargs['social'] = social

        instance._content = jinja2_template.render(**kwargs)


def register():
    signals.content_object_init.connect(execjinja2)
