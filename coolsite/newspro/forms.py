from django import forms
from django.core.exceptions import ValidationError

from .models import News



class NewsForm(forms.ModelForm):
   class Meta:
       model = News
       fields = [
           'title',
           'text',
           'category',
       ]

   def clean_name(self):
       name = self.cleaned_data["name"]
       if name[0].islower():
           raise ValidationError(
               "Название должно начинаться с заглавной буквы"
           )
       return name