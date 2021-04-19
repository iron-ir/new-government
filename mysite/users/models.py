from _blake2 import blake2b

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.db import models
from django.contrib.auth.models import AbstractUser


@deconstructible
class UnicodePhonenumberValidator(validators.RegexValidator):
    regex = r'^(\+98|0)?9\d{9}$'
    message = (
        'Enter a valid phonenumber.'
    )
    flags = 0


@deconstructible
class UnicodeNationalcodeValidator(validators.RegexValidator):
    regex = r'^\d{10}$'
    message = (
        'Enter a valid nationalcode.'
    )
    flags = 0


class User(AbstractUser):
    phonenumber_validator = UnicodePhonenumberValidator()
    phonenumber = models.CharField(
        verbose_name='شماره تلفن',
        max_length=16,
        unique=True,
        validators=[phonenumber_validator],
        blank=True,
        null=True,
    )
    is_candidate = models.BooleanField(
        default=False,
        verbose_name='کاندید',
    )
    nationalcode_validator = UnicodeNationalcodeValidator()
    nationalcode = models.CharField(
        verbose_name='شماره ملی',
        max_length=10,
        unique=True,
        validators=[nationalcode_validator],
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        verbose_name='تاریخ تولد',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class WorkExperition(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
        blank=False,
        null=False,
    )
    post_title = models.CharField(
        verbose_name='عنوان جایگاه',
        max_length=128,
        blank=False,
        null=False,
    )
    COOPERATION_TYPE_CHOICES = (
        ('1', 'پاره وقت'),
        ('2', 'تمام وقت'),
        ('3', 'مشاوره'),
    )
    cooperation_type = models.CharField(
        verbose_name='نوع همکاری',
        max_length=10,
        choices=COOPERATION_TYPE_CHOICES,
        blank=True,
        null=True,
    )
    from_date = models.DateField(
        verbose_name='از تاریخ',
        blank=True,
        null=True,
    )
    to_date = models.DateField(
        verbose_name='تا تاریخ',
        blank=True,
        null=True,
    )
    ACTIVITY_TYPE_CHOICES = (
        ('1', 'قراردادی'),
        ('2', 'پیمانی'),
        ('3', 'رسمی'),
    )
    activity_type = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=ACTIVITY_TYPE_CHOICES,
        verbose_name='نوع فعالیت',
    )
    organization_name = models.CharField(
        max_length=128,
        blank=True,
        null=True,
        verbose_name='نام سازمان'
    )

    class Meta:
        verbose_name = 'سابقه کاری'
        verbose_name_plural = 'سوابق کاری'

    def __str__(self):
        return f'{self.user}: {self.post_title}'


class Role(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=128,
    )
    is_active = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.title


class UserRole(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    role = models.ForeignKey(
        to=Role,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    from_date_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    to_date_time = models.DateTimeField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.user}: {self.role}'
