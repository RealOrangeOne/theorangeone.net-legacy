from django.conf.urls import include, url
from django.contrib import admin
from project.pages.views import Custom404View

urlpatterns = [
    url(r'^site-admin/', include(admin.site.urls)),
    url(r'^student-robotics/', include('project.robotics.urls', namespace='robotics')),
    url(r'^projects/', include('project.projects.urls', namespace='projects')),
    url(r'^media/', include('project.media.urls', namespace='media')),
    url(r'^setup/', include('project.setup.urls', namespace='setup')),
    url(r'^college/', include('project.college.urls', namespace='college')),
    url(r'', include('project.pages.urls', namespace='pages'))
]

handler404 = Custom404View