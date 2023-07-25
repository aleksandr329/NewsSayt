from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey('Categoryes', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])

class Categoryes(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat_detail', args=[str(self.id)])

