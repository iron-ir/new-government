from django.db import models
from django.contrib.auth.models import AbstractUser
from repository.uploader import image_upload_to, file_upload_to
from repository.regular_expression import UnicodeNationalcodeValidator, UnicodePhoneNumberValidator
from repository.choices import *
from base_information_setting.models import BaseInformation,BaseInformationHeader,Zone


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
        verbose_name='عکس پروفایل',
        null=True,
        blank=True,
        upload_to=image_upload_to,
    )

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Candidate(models.Model):
    user = models.OneToOneField(
        verbose_name='کاربر',
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    first_name = models.CharField(
        verbose_name='نام',
        max_length=32,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        verbose_name='نام خانوادگی',
        max_length=32,
        null=False,
        blank=False,
    )
    _gender = models.CharField(
        verbose_name='جنسیت',
        max_length=1,
        default=GENDER_DEFAULT,
        choices=GENDER_CHOICES,
        null=False,
        blank=False,
    )

    @property
    def gender(self):
        return GENDER_RETURNER(self._gender)

    @gender.setter
    def gender(self, value):
        self._gender = value

    _national_code_validator = UnicodeNationalcodeValidator()
    national_code = models.CharField(
        verbose_name='کد ملی',
        max_length=16,
        null=False,
        blank=False,
        validators=[_national_code_validator],
    )
    father_name = models.CharField(
        verbose_name='نام پدر',
        max_length=32,
        null=False,
        blank=False,
    )
    birth_date = models.DateField(
        verbose_name='تاریخ تولد',
        blank=False,
        null=False,
    )
    birth_place = models.ForeignKey(
        verbose_name='محل تولد',
        to=Zone,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    nationality = models.ForeignKey(
        verbose_name='ملیت',
        to=BaseInformation,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='bi_c_nationality',
    )
    religion = models.ForeignKey(
        verbose_name='دین',
        to=BaseInformation,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='bi_c_religion',
    )
    official_website = models.URLField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'نامزد'
        verbose_name_plural = 'نامزدها'


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
        max_length=64,
        blank=False,
        null=False,
    )
    cooperation_type = models.ForeignKey(
        verbose_name='نوع همکاری',
        to=BaseInformation,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='bi_we_cooperation_type',
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

    activity_type = models.ForeignKey(
        verbose_name='نوع فعالیت',
        to=BaseInformation,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='bi_we_activity_type',
    )

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


class EducationHistory(models.Model):
    user = models.ForeignKey(
        verbose_name='کاربر',
        to=User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    degree_type = models.ForeignKey(
        verbose_name='مقطع',
        to=BaseInformation,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='bi_eh_degree_type',
    )

    field_of_study = models.ForeignKey(
        verbose_name='رشته',
        to=BaseInformation,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='bi_eh_field_of_study',
    )
    place_of_study_type = models.ForeignKey(
        verbose_name='نوع موسسه',
        to=BaseInformation,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name='bi_eh_place_of_study_type',
    )
    place_of_study = models.CharField(
        verbose_name='نام موسسه',
        max_length=64,
        blank=False,
        null=False,
    )

    zone = models.ForeignKey(
        verbose_name='مکان',
        to=Zone,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    graduation_date = models.DateField(
        verbose_name='تاریخ اخذ مدرک',
        null=True,
        blank=True,
    )
    is_study = models.BooleanField(
        verbose_name='در حال تحصیل',
        default=False,
    )

    class Meta:
        verbose_name = 'سابقه تحصیلی'
        verbose_name_plural = 'سوابق تحصیلی'

    def __str__(self):
        return f'{self.user}: {self.degree_type} {self.field_of_study}'


class Standpoint(models.Model):
    candidate = models.ForeignKey(
        verbose_name='نامزد',
        to=Candidate,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    title = models.CharField(
        verbose_name='عنوان',
        max_length=128,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name='توضیحات',
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='فعال',
        default=False,
    )

    link = models.URLField(
        verbose_name='لینک',
        blank=True,
        null=True,
    )

    attachment = models.FileField(
        verbose_name='پیوست',
        blank=True,
        null=True,
        upload_to=file_upload_to,
    )

    class Meta:
        verbose_name = 'دیدگاه'
        verbose_name_plural = 'دیدگاه ها'

    def __str__(self):
        return f'{self.candidate.user}: {self.title}'


class Effect(models.Model):
    candidate = models.ForeignKey(
        verbose_name='کاربر',
        to=Candidate,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    title = models.CharField(
        verbose_name='عنوان',
        max_length=128,
        null=False,
        blank=False,
    )
    description = models.TextField(
        verbose_name='توضیحات',
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name='فعال',
        default=False,
    )
    link = models.URLField(
        verbose_name='لینک',
        blank=True,
        null=True,
    )
    attachment = models.FileField(
        verbose_name='پیوست',
        blank=True,
        null=True,
        upload_to=file_upload_to,
    )

    class Meta:
        verbose_name = 'اثر'
        verbose_name_plural = 'آثار'

    def __str__(self):
        return f'{self.candidate.user}: {self.title}'


class UserRelation(models.Model):
    candidate = models.ForeignKey(
        to=Candidate,
        on_delete=models.CASCADE,
        verbose_name='نامزد',
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
        null=False,
        blank=False,
    )
    relation_type = models.ForeignKey(
        verbose_name='نوع رابطه',
        to=BaseInformation,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    form_date = models.DateField(
        verbose_name='شروع رابطه',
        null=True,
        blank=True,
    )
    to_date = models.DateField(
        verbose_name='اتمام رابطه',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'رابطه فرد'
        verbose_name_plural = 'روابط افراد'

    def __str__(self):
        return f'{self.candidate.user}, {self.user}'


class CandidateGroup(models.Model):
    title = models.CharField(
        verbose_name='عنوان',
        null=False,
        blank=False,
        max_length=128,
    )

    class Meta:
        verbose_name = 'ائتلاف'
        verbose_name_plural = 'ائتلافات'

    def __str__(self):
        return f'{self.title}'
