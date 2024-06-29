from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from blog.models import Blog
from mailing.forms import ClientForm, MessageForm, MailingForm, MailingUpdateForm
from mailing.models import Client, Message, Mailing, LoggingMailing
from mailing.services import get_blogs_from_cache, get_mailing_count_from_cache, get_mailing_is_active_from_cache, \
    get_mailing_clients_unique_from_cache
from users.models import User


class InfoListView(LoginRequiredMixin, ListView):
    """Контроллер отображает на главной странице, количество рассылок, количество активных рассылок,
    количество уникальных клиентов и три случайные статьи из блога"""
    model = Blog
    template_name = "mailing/info_view.html"
    extra_context = {
        "main_page": "Главная страница",
        "mailing_management_service": "Сервис управления рассылками",
        "count": "Количество рассылок",
        "is_active": "Количество активных рассылок",
        "clients_unique": "Количество уникальных клиентов",
        "three_random_blog_articles": "Три случайные статьи из блога",
        "title": "Заголовок",
        "description": "Содержимое",
        "view_count": "Количество просмотров",

    }

    def get_queryset(self):
        queryset = super().get_queryset()
        return Blog.objects.all()[:3]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mailing_count"] = get_mailing_count_from_cache()
        context["mailing_is_active"] = get_mailing_is_active_from_cache()
        context["mailing_clients_unique"] = get_mailing_clients_unique_from_cache()
        return context


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создает клиента сервиса"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client-list")
    extra_context = {
        "title_page_create": "Добавить клиента",
        "back": "Назад",
    }

    def form_valid(self, form):
        client = form.save(commit=False)
        client.owner = self.request.user
        client.save()
        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер отображает клиентов сервиса"""
    model = Client
    extra_context = {
        "title_page": "Список клиентов",
        "email": "Почта",
        "last_name": "Фамилия",
        "view": "Посмотреть",
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(owner=user)
        return queryset


class ClientDetailView(LoginRequiredMixin, DetailView):
    """Контроллер отображает подробную информацию о клиенте"""
    model = Client
    extra_context = {
        "email": "Почта",
        "last_name": "Фамилия",
        "first_name": "Имя",
        "middle_name": "Отчество",
        "comment": "Комментарий",
        "back": "Назад",
        "update": "Изменить",
        "delete": "Удалить",
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user:
            return self.object
        raise PermissionDenied


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер изменяет данные о клиенте"""
    model = Client
    form_class = ClientForm
    extra_context = {
        "title_page_update": "Изменить клиента",
        "back": "Назад",
    }

    def get_success_url(self):
        return reverse("mailing:client-detail", args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user:
            return self.object
        raise PermissionDenied


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаляет клиента"""
    model = Client
    success_url = reverse_lazy("mailing:client-list")
    extra_context = {
        "title_page": "Удаление клиента",
        "delete_client": "Удалить клиента",
        "delete": "Удалить",
        "cancel": "Отмена",
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user:
            return self.object
        raise PermissionDenied


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создает сообщение"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message-list")
    extra_context = {
        "create_message": "Добавить письмо",
        "back": "Назад",
    }

    def form_valid(self, form):
        message = form.save(commit=False)
        message.owner = self.request.user
        message.save()
        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    """Контроллер отображает список сообщений"""
    model = Message
    extra_context = {
        "title_page_message_list": "Список писем",
        "subject_message": "Тема сообщения",
        "view": "Посмотреть",
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(owner=user)
        return queryset


class MessageDetailView(LoginRequiredMixin, DetailView):
    """Контроллер отображает детальную информацию о сообщении"""
    model = Message
    extra_context = {
        "subject_message": "Тема сообщения",
        "body_message": "Тело сообщения",
        "back": "Назад",
        "update": "Изменить",
        "delete": "Удалить",
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user:
            return self.object
        raise PermissionDenied


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер обновляет данные сообщения"""
    model = Message
    form_class = MessageForm
    extra_context = {
        "update_message": "Изменить письмо",
        "back": "Назад",
    }

    def get_success_url(self):
        return reverse("mailing:message-detail", args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user:
            return self.object
        raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаляет сообщение"""
    model = Message
    success_url = reverse_lazy("mailing:message-list")
    extra_context = {
        "title_page_delete_message": "Удаление сообщения",
        "delete_message": "Удалить сообщение",
        "delete": "Удалить",
        "cancel": "Отмена",
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user:
            return self.object
        raise PermissionDenied


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создает рассылку"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing-list")
    extra_context = {
        "create_mailing": "Добавить рассылку",
        "back": "Назад",
    }

    def form_valid(self, form):
        mailing = form.save(commit=False)
        mailing.owner = self.request.user
        mailing.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["owner"] = self.request.user
        return kwargs


class MailingListView(LoginRequiredMixin, ListView):
    """Контроллер отображает список рассылок"""
    model = Mailing
    extra_context = {
        "title": "Список рассылок",
        "name": "Название рассылки",
        "status_mailing": "Статус рассылки",
        "owner": "Владелец",
        "is_active": "Активная",
        "True": "Да",
        "False": "Нет",
        "view": "Посмотреть",
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser or user.groups.filter(name="manager"):
            queryset = queryset
        else:
            queryset = queryset.filter(owner=self.request.user)
        return queryset


class MailingDetailView(LoginRequiredMixin, DetailView):
    """Контроллер отображает детальную информацию о рассылке"""
    model = Mailing
    extra_context = {
        "name": "Название рассылки",
        "clients": "Клиенты",
        "message": "Сообщение",
        "start_mailing": "Дата и время первой отправки рассылки",
        "period": "Периодичность рассылки",
        "status_mailing": "Статус рассылки",
        "back": "Назад",
        "update": "Изменить",
        "delete": "Удалить",
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user or user.groups.filter(name="manager"):
            return self.object
        raise PermissionDenied


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер обновляет данные о рассылке"""
    model = Mailing
    form_class = MailingUpdateForm
    extra_context = {
        "update_mailing": "Изменить рассылку",
        "back": "Назад",
    }

    def get_success_url(self):
        return reverse("mailing:mailing-detail", args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user:
            return self.object
        raise PermissionDenied

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["owner"] = self.request.user
        return kwargs


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер удаляет рассылку"""
    model = Mailing
    success_url = reverse_lazy("mailing:mailing-list")
    extra_context = {
        "title_page": "Удаление рассылки",
        "delete_mailing": "Удалить рассылку",
        "delete": "Удалить",
        "cancel": "Отмена",
    }

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if user.is_superuser or self.object.owner == user:
            return self.object
        raise PermissionDenied


class LoggingMailingCreateView(CreateView):
    """Контроллер создает логи"""
    model = LoggingMailing


class LoggingMailingListView(ListView):
    """Контроллер отображает список логов"""
    model = LoggingMailing


class LoggingMailingDetailView(DetailView):
    """Котроллер отображает подробную информацию о логах"""
    model = LoggingMailing


class ManagerListView(LoginRequiredMixin, ListView):
    """Контроллер отображает список пользователей менеджеру"""
    model = User
    template_name = "mailing/manager_list.html"
    extra_context = {
        "user_page": "Список пользователей",
        "user_list": "Список пользователей",
        "email": "Почта",
        "last_name": "Фамилия",
        "first_name": "Имя",
        "middle_name": "Отчество",
        "not_specified": "Не указано",
        "is_active": "Активный",
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            queryset = queryset
        else:
            queryset = queryset.filter(is_staff=False)
        return queryset


def switcher_user_active(request, pk):
    """Функция переключает активность пользователя"""
    user_active = get_object_or_404(User, pk=pk)
    if user_active.is_active:
        user_active.is_active = False
    else:
        user_active.is_active = True
    user_active.save()
    return redirect(reverse("mailing:manager"))


def switcher_mailing_active(request, pk):
    """Функция переключает рассылку"""
    mailing_active = get_object_or_404(Mailing, pk=pk)
    if mailing_active.is_active:
        mailing_active.is_active = False
    else:
        mailing_active.is_active = True
    mailing_active.save()
    return redirect(reverse("mailing:mailing-list"))
