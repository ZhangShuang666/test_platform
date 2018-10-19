from django import forms
from django.forms import ModelForm


class ProjectForms(forms.Form):
    name = forms.CharField(label='名称', max_length=100)
    description = forms.CharField(label='描述', widget=forms.Textarea)