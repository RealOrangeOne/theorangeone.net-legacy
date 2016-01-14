class ContactForm(forms.Form):
    email = forms.CharField(label="Email Address", widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'placeholder': 'Enter your message here'}))

    def send_email(self):
        print("Sending email with", self.cleaned_data)
