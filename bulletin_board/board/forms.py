from django.forms import ModelForm, HiddenInput
from .models import Ad, Response


class AdForm(ModelForm):

    class Meta:
        model = Ad
        fields = ['author', 'article', 'categories', 'text_ad']

        widgets = {
            'author': HiddenInput()
        }


class ResponseForm(ModelForm):

    class Meta:
        model = Response
        fields = ['user', 'ads', 'text_response']

        widgets = {
            'user': HiddenInput(),
            'ads': HiddenInput(),
        }
        labels = {
            'text_response': '',
        }
