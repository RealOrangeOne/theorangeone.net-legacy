from django.conf.urls import url
from .views import StudentServerView


urlpatterns = [
    url(r'^student-server', StudentServerView.as_view(), name='student-server')
]
