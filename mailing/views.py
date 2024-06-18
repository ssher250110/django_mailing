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


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = "__all__"

    def get_success_url(self):
        return reverse("mailing:client-detail", args=[self.kwargs.get('pk')])


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client-list")


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailing:message-list")


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = "__all__"

    def get_success_url(self):
        return reverse("mailing:message-detail", args=[self.kwargs.get('pk')])


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailing:message-list")


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
    fields = "__all__"

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
