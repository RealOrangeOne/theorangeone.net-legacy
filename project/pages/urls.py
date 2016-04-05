from django.conf.urls import url
from .views import page_view, AboutView


urlpatterns = [
    url(r'^about/?$', AboutView.as_view(), name='about'),
    url(r'^(?P<path>.*)', page_view, name='page'),
]
