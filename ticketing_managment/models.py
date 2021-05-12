from django.db import models
from users.models import User
from base_information_settings.models import BaseInformation


class Ticket(models.Model):
    sender = models.ForeignKey(
        to=User,
        verbose_name='ارسال کننده',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='u_sm_sender',
    )
    t_type = models.ForeignKey(
        to=BaseInformation,
        verbose_name='نوع',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    title = models.CharField(
        verbose_name='عنوان',
        null=True,
        blank=True,
    )
    text = models.TextField(
        verbose_name='متن',
        null=True,
        blank=True,
    )
    file = models.FilePathField(
        verbose_name='فایل',
        null=True,
        blank=True,
    )
    send = models.BooleanField(
        verbose_name='ارسال شد',
        default=False,
    )
    received = models.BooleanField(
        verbose_name='دریافت شد',
        default=False,
    )
    read = models.BooleanField(
        verbose_name='خوانده شد',
        default=False,
    )
    pending = models.BooleanField(
        verbose_name='در حال بررسی',
        default=False,
    )
    checked_out = models.BooleanField(
        verbose_name='بررسی شد',
        default=False,
    )
