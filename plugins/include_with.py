# -*- coding: utf-8 -*-
"""
    # Jinja-IncludeWith

    A Jinja2 preprocessor extension that let you update the `include`
    context like this:

        {% include "something.html" with foo=bar %}
        {% include "something.html" with a=3, b=2+2, c='yes' %}

    You **must** also include 'jinja2.ext.with_' in the extensions list.

    :copyright: [Juan-Pablo Scaletti] (http://jpscaletti.com).
    :license: [MIT] (http://www.opensource.org/licenses/mit-license.php).

    Copied from https://github.com/jpscaletti/jinja-includewith due to not pip-installable

"""
import re

from jinja2.ext import Extension


__version__ = '0.1'

rx = re.compile(r'\{\%\s*include\s+(?P<tmpl>[^\s]+)\s+with\s+(?P<context>.*?)\s*\%\}',
                re.IGNORECASE)


class IncludeWith(Extension):

    def preprocess(self, source, name, filename=None):
        lastpos = 0
        while 1:
            m = rx.search(source, lastpos)
            if not m:
                break

            lastpos = m.end()
            d = m.groupdict()
            context = d['context'].strip()
            if context == 'context':
                continue

            source = ''.join([
                source[:m.start()],
                '{% with ', context, ' %}',
                '{% include ', d['tmpl'].strip(), ' %}',
                '{% endwith %}',
                source[m.end():]
            ])

        return source
