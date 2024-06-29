from django.contrib import admin
from django.contrib.admin import action

from mailing.models import Client, Message, Mailing, LoggingMailing


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("pk", "email", "last_name", "first_name", "middle_name", "comment", "owner",)
    search_fields = ("email", "last_name", "comment",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("pk", "subject", "body", "owner",)
    search_fields = ("subject",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "get_clients", "message", "start_mailing", "period", "status_mailing", "owner",)
    list_filter = ("name", "start_mailing", "period", "status_mailing",)
    search_fields = ("name", "start_mailing", "period", "status_mailing",)

    @action(description="Клиенты")
    def get_clients(self, obj):
        return "\n".join([str(c) for c in obj.clients.all()])


@admin.register(LoggingMailing)
class LoggingMailingAdmin(admin.ModelAdmin):
    list_display = ("pk", "mailing", "last_attempt_mailing", "status_attempt", "response",)
    list_filter = ("last_attempt_mailing", "status_attempt",)
    search_fields = ("last_attempt_mailing", "status_attempt",)
