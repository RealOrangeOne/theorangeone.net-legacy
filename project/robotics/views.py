from django.views.generic import TemplateView
from project.common.views import CustomHeaderBG


class RoboticsIndexView(TemplateView):
    template_name = 'robotics/index.html'

# 2015
class Index2015View(CustomHeaderBG.Template):
    template_name = 'robotics/2015-index.html'
    header_BG = "https://farm8.staticflickr.com/7711/17122633430_7d1bde923a_k.jpg"


class Robot2015View(CustomHeaderBG.Template):
    template_name = 'robotics/2015-robot.html'
    header_BG = ""


# 2014
class Index2014View(CustomHeaderBG.Template):
    template_name = 'robotics/2014-index.html'
    header_BG = "nothing"