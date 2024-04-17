import smtplib

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from mailings.models import SettingsMailing, LogsMailing


def day_mailing():
    mailings = SettingsMailing.objects.filter(period="ежедневно").filter(status="запущена")
    send_mailing(mailings)


def weekly_mailing():
    mailings = SettingsMailing.objects.filter(period="еженедельно").filter(status="запущена")
    send_mailing(mailings)


def monthly_mailing():
    mailings = SettingsMailing.objects.filter(period="раз в месяц").filter(status="запущена")
    send_mailing(mailings)


def send_mailing(mailings):
    now = timezone.now()
    for mailing in mailings:
        clients = [client.email for client in mailing.clients.all()]
        try:
            server_response = send_mail(subject=mailing.message_set.theme,
                                        message=mailing.message_set.body,
                                        from_email=settings.EMAIL_HOST_USER,
                                        recipient_list=clients,
                                        fail_silently=False)
            log = LogsMailing.objects.create(date_time_last_attempt=now,
                                       answer_server=server_response,
                                       is_status=True,
                                       mailing=mailing)
            log.save()
        except smtplib.SMTPException as e:
            log = LogsMailing.objects.create(date_time_last_attempt=now,
                                       answer_server=e,
                                       is_status=False,
                                       mailing=mailing)
            log.save()
        except Exception as e:
            log = LogsMailing.objects.create(date_time_last_attempt=now,
                                       answer_server=e,
                                       is_status=False,
                                       mailing=mailing)
            log.save()
        return log
