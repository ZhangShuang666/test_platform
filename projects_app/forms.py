from django import forms
from django.forms import ModelForm
from .models import Project


class ProjectForms(ModelForm):
    class Meta:
        model = Project
        exclude = ['create_time']