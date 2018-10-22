from django import forms
from django.forms import ModelForm
from .models import Project, Module


class ProjectForms(ModelForm):
    class Meta:
        model = Project
        exclude = ['create_time']


class ModuleForms(ModelForm):
    class Meta:
        model = Module
        exclude = ['create_time']
