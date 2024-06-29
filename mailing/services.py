import smtplib
from datetime import datetime

import pytz

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail

from blog.models import Blog
from config.settings import CACHE_ENABLED

from mailing.models import LoggingMailing, Mailing


def send_mailing(mailing):
    """Функция отправляет сообщение и записывает информацию в логи"""
    try:
        response_server = send_mail(
            subject=mailing.message.subject,
            message=mailing.message.body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[client.email for client in mailing.clients.all()],
            fail_silently=False,
        )
        logging_mailing = LoggingMailing.objects.create(mailing=mailing, status_attempt=True, response=response_server)
        logging_mailing.save()
    except smtplib.SMTPException as e:
        logging_mailing = LoggingMailing.objects.create(mailing=mailing, status_attempt=False, response=e)
        logging_mailing.save()


def filters_and_sorted_mailing_by_condition():
    """Функция фильтрует рассылки по статусу и сортирует в зависимости от периода отправки сообщения,
    передает в функцию отправки"""
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = Mailing.objects.filter(is_active=True).filter(status_mailing__in=["создана", "запущена"])
    for mailing in mailings:
        logging_mailing = LoggingMailing.objects.filter(mailing=mailing).order_by("-last_attempt_mailing").first()
        if logging_mailing:
            if current_datetime > logging_mailing.last_attempt_mailing:
                if mailing.period == "раз в день":
                    if (current_datetime - logging_mailing.last_attempt_mailing).days >= 1:
                        send_mailing(mailing)
                if mailing.period == "раз в неделю":
                    if (current_datetime - logging_mailing.last_attempt_mailing).days >= 7:
                        send_mailing(mailing)
                if mailing.period == "раз в месяц":
                    if (current_datetime - logging_mailing.last_attempt_mailing).days >= 30:
                        send_mailing(mailing)
        else:
            send_mailing(mailing)
            mailing.status_mailing = "запущена"
            mailing.save()


def get_blogs_from_cache():
    """Функция получает данные о блогах из кэша, если кэш пустой, получает данные из базы данных"""
    if not CACHE_ENABLED:
        return Blog.objects.all()[:3]
    key = "blogs"
    blogs = cache.get(key)
    if blogs is not None:
        return blogs
    blogs = Blog.objects.all()[:3]
    cache.set(key, blogs)
    return blogs


def get_mailing_count_from_cache():
    """Функция получает данные о количестве рассылок из кэша, если кэш пустой, получает данные из базы данных"""
    if not CACHE_ENABLED:
        return Mailing.objects.all().count()
    key = "mailing_count"
    mailing = cache.get(key)
    if mailing is not None:
        return mailing
    mailing = Mailing.objects.all().count()
    cache.set(key, mailing)
    return mailing


def get_mailing_is_active_from_cache():
    """Функция получает данные о количестве активных рассылок из кэша, если кэш пустой,
    получает данные из базы данных"""
    if not CACHE_ENABLED:
        return Mailing.objects.filter(is_active=True).count()
    key = "mailing_is_active"
    mailing = cache.get(key)
    if mailing is not None:
        return mailing
    mailing = Mailing.objects.filter(is_active=True).count()
    cache.set(key, mailing)
    return mailing


def get_mailing_clients_unique_from_cache():
    """Функция получает данные о количестве уникальных клиентов для рассылок из кэша, если кэш пустой,
    получает данные из базы данных"""
    if not CACHE_ENABLED:
        return Mailing.objects.distinct().count()
    key = "mailing_clients_unique"
    mailing = cache.get(key)
    if mailing is not None:
        return mailing
    mailing = Mailing.objects.distinct().count()
    cache.set(key, mailing)
    return mailing
