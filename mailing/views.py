from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Message, Mailing, LoggingMailing


class InfoView(TemplateView):
    template_name = "mailing/info_view.html"


class ClientCreateView(LoginRequiredMixin, CreateView):
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
    model = Client
    extra_context = {
        "title_page": "Список клиентов",
        "email": "Почта",
        "last_name": "Фамилия",
        "view": "Посмотреть",
    }


class ClientDetailView(LoginRequiredMixin, DetailView):
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


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        "title_page_update": "Изменить клиента",
        "back": "Назад",
    }

    def get_success_url(self):
        return reverse("mailing:client-detail", args=[self.kwargs.get('pk')])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client-list")
    extra_context = {
        "title_page": "Удаление клиента",
        "delete_client": "Удалить клиента",
        "delete": "Удалить",
        "cancel": "Отмена",
    }


class MessageCreateView(LoginRequiredMixin, CreateView):
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
    model = Message
    extra_context = {
        "title_page_message_list": "Список писем",
        "subject_message": "Тема сообщения",
        "view": "Посмотреть",
    }


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    extra_context = {
        "subject_message": "Тема сообщения",
        "body_message": "Тело сообщения",
        "back": "Назад",
        "update": "Изменить",
        "delete": "Удалить",
    }


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    extra_context = {
        "update_message": "Изменить письмо",
        "back": "Назад",
    }

    def get_success_url(self):
        return reverse("mailing:message-detail", args=[self.kwargs.get('pk')])


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message-list")
    extra_context = {
        "title_page_delete_message": "Удаление сообщения",
        "delete_message": "Удалить сообщение",
        "delete": "Удалить",
        "cancel": "Отмена",
    }


class MailingCreateView(LoginRequiredMixin, CreateView):
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


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    extra_context = {
        "title": "Список рассылок",
        "name": "Название рассылки",
        "status_mailing": "Статус рассылки",
        "view": "Посмотреть",
    }


class MailingDetailView(LoginRequiredMixin, DetailView):
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


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    extra_context = {
        "update_mailing": "Изменить рассылку",
        "back": "Назад",
    }

    def get_success_url(self):
        return reverse("mailing:mailing-detail", args=[self.kwargs.get('pk')])


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing-list")
    extra_context = {
        "title_page": "Удаление рассылки",
        "delete_mailing": "Удалить рассылку",
        "delete": "Удалить",
        "cancel": "Отмена",
    }


class LoggingMailingCreateView(CreateView):
    model = LoggingMailing


class LoggingMailingListView(LoginRequiredMixin, ListView):
    model = LoggingMailing
    extra_context = {
        "title_list_logging_mailing": "Список попыток рассылок",
        "mailing": "Рассылка",
        "status_attempt": "Статус попытки",
        "successfully": "Успешно",
        "not_successfully": "Не успешно",
        "view": "Посмотреть",
    }


class LoggingMailingDetailView(DetailView):
    model = LoggingMailing
    extra_context = {
        "mailing": "Рассылка",
        "last_attempt_mailing": "Дата и время последней попытки",
        "status_attempt": "Статус попытки",
        "response": "Ответ сервера",
        "successfully": "Успешно",
        "not_successfully": "Не успешно",
        "back": "Назад",
    }
