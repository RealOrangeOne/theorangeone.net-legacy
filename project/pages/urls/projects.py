from django.conf.urls import url
from project.pages.views import projects


urlpatterns = [
    url(r'^$', projects.AllView.as_view(), name="all"),
    url(r'^(?P<project>.+)/$', projects.ProjectView.as_view(), name="project")
]
