from django.conf.urls import url
from project.pages.views import about


urlpatterns = [
    url(r'^website/$', about.WebsiteView.as_view(), name='website'),
    url(r'^me/$', about.MeView.as_view(), name='me'),
    url(r'^$', about.IndexView.as_view(), name='index'),
]
