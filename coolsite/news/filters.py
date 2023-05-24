from django_filters import FilterSet
from .models import News


class NewsFilter(FilterSet):
   class Meta:

       model = News

       fields = {

           'title': ['icontains'],

           'time_in': [
               'lt',
               'gt',
           ],
       }


class NewsFilter2(FilterSet):
   class Meta:

       model = News

       fields = {

           'title': ['icontains'],
           'text': ['icontains'],

           'time_in': [
               'lt',

           ],
       }