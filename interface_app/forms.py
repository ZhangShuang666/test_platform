from django.forms import ModelForm
from interface_app.models import TestCase


class TestCaseForms(ModelForm):
    class Meta:
        model = TestCase
        fields = ['module']