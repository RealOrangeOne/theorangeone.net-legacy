from django.conf.urls import url
from .views import Index2015View, Index2014View, RoboticsIndexView, Robot2015View


urlpatterns = [
    url(r'^$', RoboticsIndexView.as_view(), name='index' ),
    url(r'^2015', Index2015View.as_view(), name='2015-index'),
    url(r'^2015/robot', Robot2015View.as_view(), name='2015-robot'),
    url(r'^2014', Index2014View.as_view(), name='2014-index')
]
