from django import forms

from .models import User


class ContactFrom(forms.Form):
    first_cathetus = forms.IntegerField(required=True,
                                        help_text=("enter positive numbers"))
    second_cathetus = forms.IntegerField(required=True,
                                         help_text=("enter positive numbers"))


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


class TestForm(forms.Form):
    from_email = forms.EmailField(required=True)
    message = forms.CharField(required=True)
    time_to_send = forms.DateTimeField()
