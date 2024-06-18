from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import BaseCommand

from mailing.services import start_send_mailing


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler = BlockingScheduler()
        scheduler.add_job(start_send_mailing, 'interval', seconds=5)
        scheduler.start()
