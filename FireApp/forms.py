from django import forms

class UserForm(forms.Form):
    email = forms.CharField(max_length= 30)
    username = forms.CharField(max_length= 30)
    password = forms.CharField(max_length = 30)

