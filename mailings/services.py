from smtplib import SMTPException

from django.core.mail import send_mail
from django.conf import settings
import django.utils.timezone
from django.utils import timezone

from mailings.models import Client, Message, SettingsMailing, LogsMailing


def day_mailing():
    SettingsMailing.objects.filter(period="ежедневно")
    print("Every day")


def weekly_mailing():
    SettingsMailing.objects.filter(period="еженедельно")
    print("Every week")


def monthly_mailing():
    SettingsMailing.objects.filter(period="раз в месяц")
    print("Every month")


def send_mailing():
    pass
