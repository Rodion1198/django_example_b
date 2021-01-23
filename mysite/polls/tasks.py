from datetime import datetime

from celery import shared_task
from django.core.mail import send_mail as my_send_mail


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task()
def send_email(from_email, message, time_to_send):
    my_send_mail(from_email, message, time_to_send, ['admin@example.com'])
