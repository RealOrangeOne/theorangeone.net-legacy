from django.conf.urls import include, url
from .views import page_view, index_view


urlpatterns = [
    url(r'^(?P<path>.*)/', page_view, name='page'),
    url(r'^$', index_view, name='page'),
]
