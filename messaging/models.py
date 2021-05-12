from django.db import models
from users.models import User


class Message(models.Model):
    sender = models.ForeignKey(
        to=User,
        verbose_name='ارسال کننده',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='u_m_sender',
    )
    receiver = models.ForeignKey(
        to=User,
        verbose_name='دریافت کننده',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='u_m_receiver',
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
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return f'{self.title}'

    def to_dict(self):
        return {
            'id': self.pk,
            'sender': self.sender_id,
            'receiver': self.receiver_id,
            'title': self.title,
            'text': self.text,
            'file': self.file,
            'send': self.send,
            'received': self.received,
            'read': self.read,
        }
