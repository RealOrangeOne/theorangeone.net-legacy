from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from project.pages.views import Custom404View


urlpatterns = [
    url(r'^site-admin/', include(admin.site.urls)),
    url(r'^404/', TemplateView.as_view(template_name='core/404.html')),
    url(r'', include('project.pages.urls', namespace='pages'))
]


handler404 = Custom404View
