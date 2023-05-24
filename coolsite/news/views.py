from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import NewsForm
from .models import News
from .filters import NewsFilter, NewsFilter2


class NewsList(ListView):
    model = News
    ordering = 'title'
    template_name = 'page1.html'
    context_object_name = 'news_all'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.utcnow()
        context['all'] = News.objects.all()
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'page2.html'
    context_object_name = 'news_get'



class NewsCreate(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'page3.html'


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'page3.html'



class NewsDelete(DeleteView):
    model = News
    template_name = 'page4.html'
    success_url = reverse_lazy('news_list')


class NewsSearch(ListView):
    model = News
    ordering = 'title'
    template_name = 'page5.html'
    context_object_name = 'news_all'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter2(self.request.GET, queryset)
        return self.filterset.qs



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.utcnow()
        context['all'] = News.objects.all()
        context['filterset'] = self.filterset
        return context