from django.core import validators
from django.utils.deconstruct import deconstructible
from django.db import models
from django.contrib.auth.models import AbstractUser


def _get_upload_to(instance, file_name):
    from uuid import uuid4

    _uuid = uuid4()
    _uuid2 = uuid4()
    ext = file_name.split('.')[-1]
    return "child/{}/{}.{}".format(str(_uuid), str(_uuid2), ext)


@deconstructible
class _UnicodePhonenumberValidator(validators.RegexValidator):
    regex = r'^(\+98|0)?9\d{9}$'
    message = (
        'Enter a valid phonenumber.'
    )
    flags = 0


@deconstructible
class _UnicodeNationalcodeValidator(validators.RegexValidator):
    regex = r'^\d{10}$'
    message = (
        'Enter a valid nationalcode.'
    )
    flags = 0


class User(AbstractUser):
    _phonenumber_validator = _UnicodePhonenumberValidator()
    phonenumber = models.CharField(
        verbose_name='شماره تلفن',
        max_length=16,
        unique=True,
        validators=[_phonenumber_validator],
        blank=True,
        null=True,
    )
    is_candidate = models.BooleanField(
        default=False,
        verbose_name='کاندید',
    )
    _nationalcode_validator = _UnicodeNationalcodeValidator()
    nationalcode = models.CharField(
        verbose_name='شماره ملی',
        max_length=10,
        unique=True,
        validators=[_nationalcode_validator],
        null=True,
        blank=True,
    )
    birthday = models.DateField(
        verbose_name='تاریخ تولد',
        null=True,
        blank=True,
    )
    avatar = models.ImageField(
        blank=True,
        verbose_name='عکس پروفایل',
        upload_to=_get_upload_to,
    )
    GENDER_CHOICES = (
        ('m', 'آقا'),
        ('f', 'خانوم'),
    )
    _gender = models.CharField(
        verbose_name='جنسیت',
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
        default='m',
    )

    @property
    def gender(self):
        return 'آقا' if self._gender == 'm' else 'خانوم'

    @gender.setter
    def gender(self, value):
        self._gender = value

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
    _COOPERATION_TYPE_CHOICES = (
        ('1', 'پاره وقت'),
        ('2', 'تمام وقت'),
        ('3', 'مشاوره'),
    )
    _cooperation_type = models.CharField(
        verbose_name='نوع همکاری',
        max_length=10,
        choices=_COOPERATION_TYPE_CHOICES,
        blank=True,
        null=True,
    )

    @property
    def cooperation_type(self):
        c_type = self._cooperation_type
        if c_type == '1':
            return 'پاره وقت'
        if c_type == '2':
            return 'تمام وقت'
        if c_type == '3':
            return 'مشاوره'

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
    _ACTIVITY_TYPE_CHOICES = (
        ('1', 'قراردادی'),
        ('2', 'پیمانی'),
        ('3', 'رسمی'),
    )
    _activity_type = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=_ACTIVITY_TYPE_CHOICES,
        verbose_name='نوع فعالیت',
    )

    @property
    def activity_type(self):
        c_type = self._activity_type
        if c_type == '1':
            return 'قرار دادی'
        if c_type == '2':
            return 'پیمانی'
        if c_type == '3':
            return 'رسمی'

    @activity_type.setter
    def activity_type(self, value):
        self._activity_type = value

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


class VCode(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    vcode = models.CharField(
        max_length=5,
        null=False,
        blank=False,
        editable=False
    )
    expiration_date = models.DateTimeField()
    valid = models.BooleanField(default=False)

    @staticmethod
    def get_new_vcode(user: User = None):
        vc = VCode()
        from django.utils import timezone
        import random
        now = timezone.now()
        delta = timezone.timedelta(minutes=10)
        vc.expiration_date = now + delta
        vcode = random.randint(10000, 99999)
        vc.vcode = str(vcode)
        vc.valid = True
        if user is not None:
            vc.user = user
        return vc

    def __str__(self):
        return 'Expiration date: {}'.format(self.expiration_date)

    def is_valid(self, user):
        if user == self.user:
            from django.utils import timezone
            now = timezone.now()
            return self.expiration_date > now and self.valid
        else:
            return False
