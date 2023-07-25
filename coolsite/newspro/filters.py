from django_filters import FilterSet
from .models import News


class NewsFilter(FilterSet):
   class Meta:

       model = News
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'title': ['icontains'],
           # количество товаров должно быть больше или равно

           'time_in': [
               'lt',  # цена должна быть меньше или равна указанной
               'gt',  # цена должна быть больше или равна указанной
           ],
       }