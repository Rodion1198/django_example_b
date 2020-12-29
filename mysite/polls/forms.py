from django import forms


class ContactFrom(forms.Form):
    first_cathetus = forms.IntegerField(required=True)
    second_cathetus = forms.IntegerField(required=True)
