from django.conf.urls import include, url
from django_client_reverse import urls as reverse_urls
from project.pages.views.core import Custom404View, NoJavascriptView


urlpatterns = [
    url(r'^reverse/$', include(reverse_urls, namespace='reverser')),
    url(r'^404/', Custom404View.as_view(), name="404"),
    url(r'^no-js/', NoJavascriptView.as_view(), name="no-js"),
    url(r'', include('project.pages.urls', namespace='pages'))
]

# handler404 = Custom404View
