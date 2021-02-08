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
