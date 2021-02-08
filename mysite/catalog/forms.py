from datetime import timedelta

from django import forms
from django.utils import timezone


class TestForm(forms.Form):
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    time_to_send = forms.DateTimeField(required=True, input_formats=['2006-10-25 14:30'])

    def clean_time_to_send(self):
        data = self.cleaned_data['time_to_send']

        if data <= timezone.now():
            raise forms.ValidationError('Invalid input - date can\'t be in the past')

        if data > (timezone.now() + timedelta(days=2)):
            raise forms.ValidationError('Invalid input - date can\'t be 2 days ahead')

        return data
