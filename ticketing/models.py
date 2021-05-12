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
        max_length=64,
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

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'

    def __str__(self):
        return f'{self.title}'

    def to_dict(self):
        return {
            'id': self.pk,
            'sender': self.sender_id,
            't_type': self.t_type_id,
            'title': self.title,
            'text': self.text,
            'file': self.file,
            'send': self.send,
            'received': self.received,
            'read': self.read,
            'pending': self.pending,
            'checked_out': self.checked_out,
        }


class Answer(models.Model):
    ticket = models.ForeignKey(
        to=Ticket,
        verbose_name='تیکت',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
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
        max_length=64,
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

    class Meta:
        verbose_name = 'پاسخ'
        verbose_name_plural = 'پاسخ ها'

    def __str__(self):
        return f'{self.title}'

    def to_dict(self):
        return {
            'id': self.pk,
            'ticket': self.ticket_id,
            't_type': self.t_type_id,
            'title': self.title,
            'text': self.text,
            'file': self.file,
            'send': self.send,
            'received': self.received,
            'read': self.read,
        }
