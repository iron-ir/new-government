from django.db import models
from users.models import User
from base_information_settings.models import BaseInformation


class ShortMessage(models.Model):
    sender = models.ForeignKey(
        to=User,
        verbose_name='ارسال کننده',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='u_sm_sender',
    )
    receiver = models.ForeignKey(
        to=User,
        verbose_name='دریافت کننده',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='u_sm_receiver',
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


class Message(models.Model):
    sender = models.ForeignKey(
        to=User,
        verbose_name='ارسال کننده',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='u_sm_sender',
    )
    receiver = models.ManyToManyField(
        to=User,
        verbose_name='دریافت کننده ها',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='u_sm_receiver',
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

