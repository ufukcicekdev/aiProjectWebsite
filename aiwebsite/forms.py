from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, error_messages={'required': 'Name field cannot be empty.'})
    email = forms.EmailField(label='Your Email Address', error_messages={'required': 'Email field cannot be empty.', 'invalid': 'Please enter a valid email address.'})
    message = forms.CharField(label='Your Message', widget=forms.Textarea, error_messages={'required': 'Message field cannot be empty.'})
