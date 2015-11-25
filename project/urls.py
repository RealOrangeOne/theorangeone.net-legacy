from django.conf.urls import include, url
from django.contrib import admin
from project.pages.views import Custom404View, NoJavascriptView


urlpatterns = [
    url(r'^site-admin/', include(admin.site.urls)),
    url(r'^404/', Custom404View.as_view(), name="404"),
    url(r'^404/', Custom404View.as_view(), name="404"),
    url(r'^no-js/', NoJavascriptView.as_view(), name="no-js"),
    url(r'', include('project.pages.urls', namespace='pages'))
]

handler404 = Custom404View
