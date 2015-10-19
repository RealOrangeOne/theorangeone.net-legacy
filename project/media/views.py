from django.views.generic import TemplateView
from project.common.views import CustomHeaderBG


class YoutubeView(CustomHeaderBG.Template):
    template_name = "media/youtube.html"


class GalleryView(TemplateView):
    template_name = "media/gallery.html"
