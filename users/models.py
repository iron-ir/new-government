from django.db import models
from django.contrib.auth.models import AbstractUser
from repository.regular_expression import UnicodeNationalcodeValidator, UnicodePhoneNumberValidator

from repository.choices import (
    YES_OR_NO_CHOICES,
    YES_OR_NO_RETURNER,
    GENDER_CHOICES,
    GENDER_DEFAULT,
    GENDER_RETURNER,
    VCODE_CHOICES,
    VCODE_DEFAULT,
)

from repository.uploader import image_upload_to


class User(AbstractUser):
    _verified_badge = models.BooleanField(
        verbose_name='تایید',
        help_text='مقدار این فیلد زمانی برابر با True می باشد که کاربر احراز هویت شده باشد.',
        choices=YES_OR_NO_CHOICES,
        default=False,
    )

    @property
    def verified_badge(self):
        return YES_OR_NO_RETURNER(self._verified_badge)

    @verified_badge.setter
    def verified_badge(self, value):
        self._verified_badge = value

    _phone_number_validator = UnicodePhoneNumberValidator()
    phone_number = models.CharField(
        verbose_name='شماره تلفن',
        max_length=16,
        unique=True,
        validators=[_phone_number_validator],
        blank=True,
        null=True,
    )
    _is_phone_number_verify = models.BooleanField(
        verbose_name='تایید شماره تلفن',
        choices=YES_OR_NO_CHOICES,
        default=False,
    )

    @property
    def is_phone_number_verify(self):
        return YES_OR_NO_RETURNER(self._is_phone_number_verify)

    @is_phone_number_verify.setter
    def is_phone_number_verify(self, value):
        self._is_phone_number_verify = value

    _national_code_validator = UnicodeNationalcodeValidator()
    national_code = models.CharField(
        verbose_name='شماره ملی',
        max_length=10,
        unique=True,
        validators=[_national_code_validator],
        null=True,
        blank=True,
    )
    _is_national_code = models.BooleanField(
        verbose_name='تایید شماره ملی',
        choices=YES_OR_NO_CHOICES,
        default=False,
    )

    @property
    def is_national_code(self):
        return YES_OR_NO_RETURNER(self._is_national_code)

    @is_national_code.setter
    def is_national_code(self, value):
        self._is_national_code = value

    birth_date = models.DateField(
        verbose_name='تاریخ تولد',
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        blank=True,
        null=True,
        verbose_name='عکس پروفایل',
        upload_to=image_upload_to,
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


# class WorkExperition(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         verbose_name='کاربر',
#         blank=False,
#         null=False,
#     )
#     post_title = models.CharField(
#         verbose_name='عنوان جایگاه',
#         max_length=128,
#         blank=False,
#         null=False,
#     )
#     _COOPERATION_TYPE_CHOICES = (
#         ('1', 'پاره وقت'),
#         ('2', 'تمام وقت'),
#         ('3', 'مشاوره'),
#     )
#     _cooperation_type = models.CharField(
#         verbose_name='نوع همکاری',
#         max_length=10,
#         choices=_COOPERATION_TYPE_CHOICES,
#         blank=True,
#         null=True,
#     )
#
#     @property
#     def cooperation_type(self):
#         c_type = self._cooperation_type
#         if c_type == '1':
#             return 'پاره وقت'
#         if c_type == '2':
#             return 'تمام وقت'
#         if c_type == '3':
#             return 'مشاوره'
#
#     @cooperation_type.setter
#     def cooperation_type(self, value):
#         self._cooperation_type = value
#
#     from_date = models.DateField(
#         verbose_name='از تاریخ',
#         blank=True,
#         null=True,
#     )
#     to_date = models.DateField(
#         verbose_name='تا تاریخ',
#         blank=True,
#         null=True,
#     )
#     _ACTIVITY_TYPE_CHOICES = (
#         ('1', 'قراردادی'),
#         ('2', 'پیمانی'),
#         ('3', 'رسمی'),
#     )
#     _activity_type = models.CharField(
#         max_length=10,
#         blank=True,
#         null=True,
#         choices=_ACTIVITY_TYPE_CHOICES,
#         verbose_name='نوع فعالیت',
#     )
#
#     @property
#     def activity_type(self):
#         c_type = self._activity_type
#         if c_type == '1':
#             return 'قرار دادی'
#         if c_type == '2':
#             return 'پیمانی'
#         if c_type == '3':
#             return 'رسمی'
#
#     @activity_type.setter
#     def activity_type(self, value):
#         self._activity_type = value
#
#     organization_name = models.CharField(
#         max_length=128,
#         blank=True,
#         null=True,
#         verbose_name='نام سازمان'
#     )
#
#     class Meta:
#         verbose_name = 'سابقه کاری'
#         verbose_name_plural = 'سوابق کاری'
#
#     def __str__(self):
#         return f'{self.user}: {self.post_title}'
#
#
# class Role(models.Model):
#     title = models.CharField(
#         null=False,
#         blank=False,
#         max_length=128,
#     )
#     is_active = models.BooleanField(
#         default=False,
#     )
#
#     def __str__(self):
#         return self.title
#
#
# class UserRole(models.Model):
#     user = models.ForeignKey(
#         to=User,
#         on_delete=models.CASCADE,
#         null=False,
#         blank=False,
#     )
#     role = models.ForeignKey(
#         to=Role,
#         on_delete=models.CASCADE,
#         null=False,
#         blank=False,
#     )
#     from_date_time = models.DateTimeField(
#         null=True,
#         blank=True,
#     )
#     to_date_time = models.DateTimeField(
#         null=True,
#         blank=True,
#     )
#
#     def __str__(self):
#         return f'{self.user}: {self.role}'
#
#
# class VCode(models.Model):
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
#     vcode = models.CharField(
#         max_length=5,
#         null=False,
#         blank=False,
#         editable=False
#     )
#     vtype = models.CharField(
#         max_length=1,
#         null=False,
#         blank=False,
#         choices=VCODE_CHOICES,
#         default=VCODE_DEFAULT,
#     )
#     expiration_date = models.DateTimeField()
#     valid = models.BooleanField(default=False)
#
#     @staticmethod
#     def get_new_vcode(user: User = None, vtype: str = None):
#         from django.utils import timezone
#         import random
#         now = timezone.now()
#         delta = timezone.timedelta(minutes=10)
#         vcode = random.randint(10000, 99999)
#         vc = VCode()
#         vc.expiration_date = now + delta
#         vc.vcode = str(vcode)
#         vc.valid = True
#         if user is not None:
#             vc.user = user
#         if vtype is not None:
#             vc.vtype = vtype
#         return vc
#
#     def __str__(self):
#         return 'Expiration date: {}'.format(self.expiration_date)
#
#     def is_valid(self, user: User, vtype: str = VCODE_DEFAULT):
#         if user == self.user:
#             if self.vtype == vtype:
#                 from django.utils import timezone
#                 now = timezone.now()
#                 return self.expiration_date > now and self.valid
#         else:
#             return False
