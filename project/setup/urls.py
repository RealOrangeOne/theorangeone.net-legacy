from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^desk', views.DeskView.as_view(), name="desk"),
    url(r'^', views.SetupIndexView.as_view(), name="index")
]
