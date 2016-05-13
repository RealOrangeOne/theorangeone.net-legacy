from django.conf.urls import include, url


urlpatterns = [
    url(r'^blog/', include('project.blog.urls', namespace='blog')),
    url(r'', include('project.pages.urls', namespace='pages'))
]
