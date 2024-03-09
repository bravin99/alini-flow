from django.core.mail import send_mail
from django_q.tasks import async_task, result
from django.contrib import messages


def send_email_with_q(subject, message, from_email, to_email):
    try:
        async_task(send_mail, subject, message, from_email,
                   [to_email])
    except Exception as e:
        pass