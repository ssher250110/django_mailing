from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name

urlpatterns = [
    path("client/create/", ClientCreateView.as_view(), name="client-create"),
    path("client/", ClientListView.as_view(), name="client-list"),
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client-detail"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),
]
