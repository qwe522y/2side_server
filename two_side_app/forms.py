from django import forms

class AddDocumentForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()
    document = forms.CharField()