from django import forms
from django_dbq.models import Job


class ContactForm(forms.Form):
    email = forms.CharField(label="Email Address", widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'placeholder': 'Enter your message here'}))

    def send_email(self):
        Job.objects.create(name='send_email', workspace={
            'context': self.cleaned_data,
            'to_email': 'info@theorangeone.net',
            'from_email': self.cleaned_data['email'],
            'template': 'email/contact_message.html'
        })
