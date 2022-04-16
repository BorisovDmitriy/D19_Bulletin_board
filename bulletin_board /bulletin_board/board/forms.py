from django.forms import ModelForm, HiddenInput
from .models import Ad
from django.db import models


class AdForm(ModelForm):

    class Meta:
        model = Ad
        fields = ['author', 'article', 'categories', 'text_ad']

    widgets = {
        'author': HiddenInput()
    }
