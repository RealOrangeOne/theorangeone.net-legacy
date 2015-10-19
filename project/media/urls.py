from django.conf.urls import url
from .views import GalleryView, YoutubeView


urlpatterns = [
    url(r'^gallery', GalleryView.as_view(), name='gallery'),
    url(r'^youtube', YoutubeView.as_view(), name='youtube')
]
