from django.conf.urls import url
from project.pages.views import projects


urlpatterns = [
    url(r'^projects/all/$', projects.AllView.as_view(), name="all"),
    url(r'^projects/(?P<project>.+)/$', projects.ProjectView.as_view(), name="project")
]
