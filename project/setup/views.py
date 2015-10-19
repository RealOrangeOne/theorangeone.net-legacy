from django.views.generic import TemplateView
from project.common.views import CustomHeaderBG


class SetupIndexView(TemplateView):
    template_name = "setup/index.html"


class DeskView(CustomHeaderBG.Template):
    template_name = "setup/my-rig.html"
    header_BG = "https://c1.staticflickr.com/1/557/18312934624_b51a541594_h.jpg"
