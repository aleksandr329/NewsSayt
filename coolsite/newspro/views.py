import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import NewsFilter
from .forms import NewsForm
from .models import News

logger = logging.getLogger(__name__)
class NewsList(ListView):
    model = News
    ordering = '-id'
    template_name = 'main.html'
    context_object_name = 'news_all'
    paginate_by = 2

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = NewsFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmark'] = News.objects.all()
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'detail.html'
    context_object_name = 'news_get'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmark'] = 'Подробное описание'
        return context



class NewsCreate(LoginRequiredMixin, CreateView):
    raise_exception = True # - это для того чтобы django выдавал ошибку 403 если пользователь не авторизирован
    # Указываем нашу разработанную форму
    form_class = NewsForm
    # модель товаров
    model = News
    # и новый шаблон, в котором используется форма.
    template_name = 'add_page.html'


class NewsUpdate(UpdateView):
    form_class = NewsForm
    model = News
    template_name = 'add_page.html'


class NewsDelete(DeleteView):
    model = News
    template_name = 'news_delet.html'
    success_url = reverse_lazy('main')

