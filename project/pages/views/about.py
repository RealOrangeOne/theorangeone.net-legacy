from project.common.views import CustomTemplate, CustomFormTemplate
from project.common.forms import ContactForm


class WebsiteView(CustomTemplate):
    template_name = 'about/website.html'
    html_title = "About website"


class IndexView(CustomFormTemplate):
    template_name = 'about/index.html'
    html_title = "About"
    success_url = '/about/?sent'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sent'] = 'sent' not in self.request.GET
        return context

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class MeView(CustomTemplate):
    template_name = 'about/me.html'
    html_title = "About Me"
