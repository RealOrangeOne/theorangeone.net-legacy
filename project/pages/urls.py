from django.conf.urls import include, url
from .views import page_view, index_view, AboutView


urlpatterns = [
    url(r'^about/?$', AboutView.as_view(), name='about'),
    url(r'^(?P<path>.*)', page_view, name='page'),
]
