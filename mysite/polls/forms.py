from django import forms


class ContactFrom(forms.Form):
    first_cathetus = forms.IntegerField(required=True,
                                        help_text=("enter positive numbers"))
    second_cathetus = forms.IntegerField(required=True,
                                         help_text=("enter positive numbers"))
