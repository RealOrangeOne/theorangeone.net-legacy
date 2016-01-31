from django.conf.urls import include, url
from django_client_reverse import urls as reverse_urls
from project.pages.views.core import Custom404View, NoJavascriptView


urlpatterns = [
    url(r'^reverse/$', include(reverse_urls, namespace='reverser')),
    url(r'^404/', Custom404View.as_view(), name="404"),
    url(r'^no-js/', NoJavascriptView.as_view(), name="no-js"),
    url(r'^about/', include('project.pages.urls.about', namespace='about')),
    url(r'^college/', include('project.pages.urls.college', namespace='colldge')),
    url(r'^core/', include('project.pages.urls.core', namespace='core')),
    url(r'^projects/', include('project.pages.urls.projects', namespace='projects')),
    url(r'^robotics/', include('project.pages.urls.robotics', namespace='robotics')),
    url(r'', include('project.pages.urls.core', namespace='pages'))
]

# handler404 = Custom404View
