from django.db import models
from django.contrib.auth.models import AbstractUser
from repository.uploader import image_upload_to
from repository.regular_expression import UnicodeNationalcodeValidator, UnicodePhoneNumberValidator
from repository.choices import *


class User(AbstractUser):
    first_name = None
    last_name = None
    _phone_number_validator = UnicodePhoneNumberValidator()
    phone_number = models.CharField(
        verbose_name='شماره تلفن',
        max_length=16,
        unique=True,
        validators=[_phone_number_validator],
        blank=True,
        null=True,
    )
    is_phone_number_verify = models.BooleanField(
        verbose_name='تایید شماره تلفن',
        default=False,
    )

    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to=image_upload_to,
        verbose_name='عکس پروفایل',
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Voter(models.Model):
    pass


class Candidate(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='کاربر',
    )
    first_name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        verbose_name='نام',
    )
    last_name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        verbose_name='نام خانوادگی',
    )
    _national_code_validator = UnicodeNationalcodeValidator()
    national_code = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        verbose_name='کد ملی',
        validators=[_national_code_validator],
    )
    father_name = models.CharField(
        max_length=32,
        null=False,
        blank=False,
        verbose_name='نام پدر',
    )
    birth_date = models.DateField(
        blank=False,
        null=False,
        verbose_name='تاریخ تولد',
    )


class WorkExpiration(models.Model):
    user = models.ForeignKey(
        verbose_name='کاربر',
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    post_title = models.CharField(
        verbose_name='عنوان جایگاه',
        max_length=128,
        blank=False,
        null=False,
    )
    _cooperation_type = models.CharField(
        verbose_name='نوع همکاری',
        max_length=10,
        choices=COOPERATION_TYPE_CHOICES,
        default=COOPERATION_TYPE_DEFAULT,
    )

    @property
    def cooperation_type(self):
        return COOPERATION_TYPE_RETURNER(self._cooperation_type)

    @cooperation_type.setter
    def cooperation_type(self, value):
        self._cooperation_type = value

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

    _activity_type = models.CharField(
        verbose_name='نوع فعالیت',
        max_length=10,
        choices=ACTIVITY_TYPE_CHOICES,
        default=ACTIVITY_TYPE_DEFAULT,
    )

    @property
    def activity_type(self):
        return ACTIVITY_TYPE_RETURNER(self._activity_type)

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value

    organization_name = models.CharField(
        verbose_name='نام سازمان',
        max_length=128,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'سابقه کاری'
        verbose_name_plural = 'سوابق کاری'

    def __str__(self):
        return f'{self.user}: {self.post_title}'
