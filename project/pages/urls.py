from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about/website/$', views.AboutWebsiteView.as_view(), name='about-website'),
    url(r'^about/me/$', views.AboutMeView.as_view(), name='about-me'),
    url(r'^about/$', views.AboutIndexView.as_view(), name='about'),
    url(r'^$', views.IndexView.as_view(), name='index')
]
