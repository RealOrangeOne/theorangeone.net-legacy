from django.views.generic import TemplateView
from project.common.views import CustomHeaderBG


# Project Views
class AllProjectsView(TemplateView):
    template_name = "projects/all_projects.html"


class AttackOnBlocksView(CustomHeaderBG.Template):
    template_name = "college/attack-on-blocks.html"


class BSODEnablerView(CustomHeaderBG.Template):
    template_name = 'projects/BSOD-Enabler.html'
    header_BG = 'http://cdn9.howtogeek.com/wp-content/uploads/2013/05/xwindows-8-blue-screen-error.png.pagespeed.ic.yOWUS_rYGn.png'


class HipChatEmoticonsForAllView(CustomHeaderBG.Template):
    template_name = 'projects/hipchat-emoticons-for-all.html'
    header_BG = "https://info.seibert-media.net/plugins/servlet/pptslide?attachment=HipChat+Server+Sales+Pitch+Final+PPT.pptx&attachmentId=7536966&attachmentVer=1&pageId=3179011&slide=0"


class PithosView(CustomHeaderBG.Template):
    template_name = 'projects/pithos.html'


# Code Views
class MorseCodeDecoderView(CustomHeaderBG.Template):
    template_name = 'projects/morse-code-decoder.html'


class WikiGameSolverView(CustomHeaderBG.Template):
    template_name = 'projects/wiki-game-solver.html'
    header_BG = "http://is1.mzstatic.com/image/pf/us/r30/Purple/v4/a3/3f/31/a33f31dd-3ace-ffe4-5531-89d3f3a1106f/mzl.ihqwkbih.png"