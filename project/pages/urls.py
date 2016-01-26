from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about/website/$', views.about.WebsiteView.as_view(), name='about-website'),
    url(r'^about/me/$', views.about.MeView.as_view(), name='about-me'),
    url(r'^about/$', views.about.IndexView.as_view(), name='about'),

    url(r'^projects/all/$', views.projects.AllView.as_view(), name="all-projects"),
    url(r'^projects/(?P<project>.+)/$', views.projects.ProjectView.as_view(), name="projects"),

    url(r'^robotics/$', views.robotics.IndexView.as_view(), name="robotics-index"),
    url(r'^robotics/2014/$', views.robotics.Index2014View.as_view(), name="robotics-2014-index"),
    url(r'^robotics/2015/robot/$', views.robotics.Robot2015View.as_view(), name="robotics-2015-robot"),
    url(r'^robotics/2015/$', views.robotics.Index2015View.as_view(), name="robotics-2015-index"),

    url(r'^$', views.core.IndexView.as_view(), name='index')
]
