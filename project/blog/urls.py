from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<slug>.+)/$', views.BlogView.as_view(), name='blog-post'),
]
