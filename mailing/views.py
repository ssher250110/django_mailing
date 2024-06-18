from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from mailing.forms import ClientForm, MessageForm, MailingForm
from mailing.models import Client, Message, Mailing, LoggingMailing


class InfoView(TemplateView):
    template_name = "mailing/info_view.html"


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client-list")
    extra_context = {
        "title_page_create": "Добавить клиента",
        "back": "Назад",
    }


class ClientListView(ListView):
    model = Client
    extra_context = {
        "title_page": "Список клиентов",
        "email": "Почта",
        "last_name": "Фамилия",
        "view": "Посмотреть",
    }


class ClientDetailView(DetailView):
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


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    extra_context = {
        "title_page_update": "Изменить клиента",
        "back": "Назад",
    }

    def get_success_url(self):
        return reverse("mailing:client-detail", args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client-list")
    extra_context = {
        "title_page": "Удаление клиента",
        "delete_client": "Удалить клиента",
        "delete": "Удалить",
        "cancel": "Отмена",
    }


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message-list")
    extra_context = {
        "create_message": "Добавить письмо",
        "back": "Назад",
    }


class MessageListView(ListView):
    model = Message
    extra_context = {
        "title_page_message_list": "Список писем",
        "subject_message": "Тема сообщения",
        "view": "Посмотреть",
    }


class MessageDetailView(DetailView):
    model = Message
    extra_context = {
        "subject_message": "Тема сообщения",
        "body_message": "Тело сообщения",
        "back": "Назад",
        "update": "Изменить",
        "delete": "Удалить",
    }


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    extra_context = {
        "update_message": "Изменить письмо",
        "back": "Назад",
    }

    def get_success_url(self):
        return reverse("mailing:message-detail", args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message-list")
    extra_context = {
        "title_page_delete_message": "Удаление сообщения",
        "delete_message": "Удалить сообщение",
        "delete": "Удалить",
        "cancel": "Отмена",
    }


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing-list")


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse("mailing:mailing-detail", args=[self.kwargs.get('pk')])


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing-list")


class LoggingMailingCreateView(CreateView):
    model = LoggingMailing


class LoggingMailingListView(ListView):
    model = LoggingMailing


class LoggingMailingDetailView(DetailView):
    model = LoggingMailing
