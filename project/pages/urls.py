from django.conf.urls import url
from .views import page_view


urlpatterns = [
    url(r'^(?P<path>.*)', page_view, name='page'),
]
