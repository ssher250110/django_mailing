from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mailing.models import Client


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
