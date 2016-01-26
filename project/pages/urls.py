from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about/website/$', views.about.WebsiteView.as_view(), name='about-website'),
    url(r'^about/me/$', views.about.MeView.as_view(), name='about-me'),
    url(r'^about/$', views.about.IndexView.as_view(), name='about'),
    url(r'^projects/all/$', views.projects.AllView.as_view(), name="all-projects"),
    url(r'^projects/(?P<project>.+)/$', views.projects.ProjectView.as_view(), name="projects"),
    url(r'^$', views.core.IndexView.as_view(), name='index')
]
