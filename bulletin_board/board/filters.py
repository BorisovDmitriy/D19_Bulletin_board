from django_filters import FilterSet, ModelChoiceFilter
from .models import Ad,Response


class NewsFilterByAd(FilterSet):
    ad_objects = ModelChoiceFilter(field_name='ad', queryset=Ad.objects.all(), label='Объявление')

    class Meta:

        model = Response

        fields = ['ad_objects']
