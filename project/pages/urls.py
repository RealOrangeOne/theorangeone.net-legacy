from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^about/website/$', views.AboutWebsiteView.as_view(), name='about-website'),
    url(r'^about/$', views.AboutIndexView.as_view(), name='about'),
    url(r'^no-js/$', views.NoJavascriptView.as_view(), name='no-js'),
    url(r'^404/$', views.Custom404View.as_view(), name='404'),
    url(r'^$', views.IndexView.as_view(), name='index')
]
