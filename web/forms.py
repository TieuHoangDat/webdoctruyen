from django import forms

class nameForm(forms.Form):
    name = forms.CharField(label="Name",max_length=10)
    age = forms.CharField(label="age", max_length=10)