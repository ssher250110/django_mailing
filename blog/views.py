from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from blog.models import Blog


class BlogListView(LoginRequiredMixin, ListView):
    """Контроллер для отображения списка блогов"""
    model = Blog
    extra_context = {
        "Blog_page": "Блог",
        "title": "Блог",
        "Not_body": "Содержимое отсутствует",
        "View": "Посмотреть",
    }


class BlogDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для отображения одного блога"""
    model = Blog
    extra_context = {
        "Blog_page": "Блог",
        "Not_body": "Содержимое отсутствует",
        "Data_creation": "Дата публикации",
        "Data_count_view": "Количество просмотров",
        "Back": "Назад",
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object
