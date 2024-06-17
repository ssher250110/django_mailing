from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import ClientListView, ClientCreateView, ClientDetailView, ClientUpdateView, ClientDeleteView, \
    MessageCreateView, MessageListView, MessageDetailView, MessageUpdateView, MessageDeleteView, \
    MailingCreateView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView, \
    LoggingMailingCreateView, LoggingMailingListView, LoggingMailingDetailView

app_name = MailingConfig.name

urlpatterns = [
    path("client/create/", ClientCreateView.as_view(), name="client-create"),
    path("client/", ClientListView.as_view(), name="client-list"),
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client-detail"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client-update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),

    path("message/create/", MessageCreateView.as_view, name="message-create"),
    path("message/", MessageListView.as_view, name="message-list"),
    path("message/<int:pk>/", MessageDetailView.as_view, name="message-detail"),
    path("message/<int:pk>/update", MessageUpdateView.as_view, name="message-update"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view, name="message-delete"),

    path("message/create/", MailingCreateView.as_view, name="mailing-create"),
    path("message/", MailingListView.as_view, name="mailing-list"),
    path("message/<int:pk>/", MailingDetailView.as_view, name="mailing-detail"),
    path("message/<int:pk>/update", MailingUpdateView.as_view, name="mailing-update"),
    path("message/<int:pk>/delete/", MailingDeleteView.as_view, name="mailing-delete"),

    path("logging/create/", LoggingMailingCreateView.as_view, name="logging-create"),
    path("loggin/", LoggingMailingListView.as_view, name="logging-list"),
    path("logging/<int:pk>/", LoggingMailingDetailView.as_view, name="loggin-detail"),
]
