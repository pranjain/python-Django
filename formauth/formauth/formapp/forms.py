from django import forms
from django.core import validators

class Employee(forms.Form):
    emp_name = forms.CharField(max_length=20)
    emp_email = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

