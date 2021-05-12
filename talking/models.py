from django.db import models
from users.models import User


class Talk(models.Model):
    owner = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='مالک',
        related_name='t_u_owner',
    )

    employees = models.ManyToManyField(
        to=User,
        related_name='t_u_employees',
    )

    is_active = models.BooleanField(
        default=False,

    )

    off_on = models.BooleanField(
        default=False,
    )

    class Meta:
        verbose_name = 'مباحثه عمومی'
        verbose_name_plural = 'مباحثات عمومی'

    def __str__(self):
        return f'{self.owner.username}'

    def to_dict(self):
        employees_id = {}
        i = 0
        for employ in self.employees.all():
            i += 1
            employees_id[f'{i}'] = employ.pk

        return {
            'id': self.pk,
            'receiver': self.owner_id,
            'employees': employees_id,
            'is_active': self.is_active,
            'off_on': self.off_on,
        }


class ShortMessage(models.Model):
    send_time = models.DateTimeField(
        verbose_name='زمان ارسال',
        null=False,
        blank=False,
    )
    sender = models.ForeignKey(
        to=User,
        verbose_name='ارسال کننده',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='u_sm_sender',
    )
    receiver = models.ForeignKey(
        to=Talk,
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
    presentable = models.BooleanField(
        verbose_name='قابل نمایش',
        default=True,
    )

    def __str__(self):
        return f'{self.sender.username}::{self.receiver.owner.username}'

    def to_dict(self):
        return {
            'id': self.pk,
            'send_time': self.send_time,
            'sender': self.sender,
            'receiver': self.receiver,
            'text': self.text,
            'file': self.file,
            'send': self.send,
            'received': self.received,
            'read': self.read,
            'presentable': self.presentable,
        }
