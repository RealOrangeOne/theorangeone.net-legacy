from django.conf.urls import url
from project.pages.views import core


urlpatterns = [
    url(r'^$', core.IndexView.as_view(), name='index')
]
