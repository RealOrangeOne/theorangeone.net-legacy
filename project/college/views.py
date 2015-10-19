from django.views.generic import TemplateView
from project.common.views import CustomHeaderBG

class StudentServerView(CustomHeaderBG.Template):
    template_name = 'college/student-server.html'