from django.conf.urls import url
from project.pages.views import robotics


urlpatterns = [
    url(r'^robotics/$', robotics.IndexView.as_view(), name="index"),
    url(r'^robotics/2014/$', robotics.Index2014View.as_view(), name="2014-index"),
    url(r'^robotics/2015/robot/$', robotics.Robot2015View.as_view(), name="2015-robot"),
    url(r'^robotics/2015/$', robotics.Index2015View.as_view(), name="2015-index")
]
