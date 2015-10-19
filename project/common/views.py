from django.views.generic import TemplateView


class CustomHeaderBG():
    """Allow custom header background"""

    class Template(TemplateView):
        header_BG = ""
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['header_BG'] = self.header_BG
            return context