from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from mailing.models import Client, Message, Mailing, LoggingMailing


class InfoView(TemplateView):
    template_name = "mailing/info_view.html"


class ClientCreateView(CreateView):
    model = Client


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client


class MessageCreateView(CreateView):
    model = Message


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message


class MessageDeleteView(DeleteView):
    model = Message


class MailingCreateView(CreateView):
    model = Mailing


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing


class MailingUpdateView(UpdateView):
    model = Mailing


class MailingDeleteView(DeleteView):
    model = Mailing


class LoggingMailingCreateView(CreateView):
    model = LoggingMailing


class LoggingMailingListView(ListView):
    model = LoggingMailing


class LoggingMailingDetailView(DetailView):
    model = LoggingMailing
