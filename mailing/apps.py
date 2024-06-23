from time import sleep

from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing"
    verbose_name = "Рассылки"

    def ready(self):
        from mailing.services import filters_and_sorted_mailing_by_condition
        sleep(2)
        filters_and_sorted_mailing_by_condition()
