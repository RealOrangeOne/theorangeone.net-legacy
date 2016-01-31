from django.conf.urls import url
from project.pages.views import college


urlpatterns = [
    url(r'^attack-on-blocks/$', college.AttackOnBlocksView.as_view(), name='attack-on-blocks'),
]
