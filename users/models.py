from django.db import models
from django.contrib.auth.models import AbstractUser
from repository.uploader import image_upload_to, file_upload_to
from repository.regular_expression import UnicodeNationalcodeValidator, UnicodePhoneNumberValidator, \
    UnicodePasswordValidator
from repository.choices import *
from base_information_setting.models import BaseInformation, BaseInformationHeader, Zone


class User(AbstractUser):
    _is_verify = models.BooleanField(
        verbose_name='تایید',
        default=False,
    )

    @property
    def is_verify(self):
        self._is_verify = self.is_email_verify and \
                          self.is_phone_number_verify and \
                          self.is_avatar_verify and \
                          self.is_birth_date_verify and \
                          self.is_birth_place_verify and \
                          self.is_father_name_verify and \
                          self.is_first_name_verify and \
                          self.is_gendre_verify and \
                          self.is_last_name_verify and \
                          self.is_mother_name_verify and \
                          self.is_national_code_verify and \
                          self.is_national_code_verify and \
                          self.is_official_website_verify and \
                          self.is_religion_verify
        return self._is_verify

    email = models.EmailField(
        verbose_name='ایمیل',
        unique=True,
        blank=True,
        null=True,
    )
    is_email_verify = models.BooleanField(
        verbose_name='تایید ایمیل',
        default=False,
    )
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
    is_avatar_verify = models.BooleanField(
        verbose_name='تایید عکس پروفایل',
        default=False,
    )
    first_name = models.CharField(
        verbose_name='نام',
        max_length=64,
        null=True,
        blank=True,
    )
    is_first_name_verify = models.BooleanField(
        verbose_name='تایید نام',
        default=False,
    )
    last_name = models.CharField(
        verbose_name='نام خانوادگی',
        max_length=64,
        null=True,
        blank=True,
    )
    is_last_name_verify = models.BooleanField(
        verbose_name='تایید نام خانوادگی',
        default=False,
    )
    _gender = models.CharField(
        verbose_name='جنسیت',
        max_length=1,
        default=GENDER_DEFAULT,
        choices=GENDER_CHOICES,
    )
    is_gendre_verify = models.BooleanField(
        verbose_name='تایید جنسیت',
        default=False,
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
        null=True,
        blank=True,
        unique=True,
        validators=[_national_code_validator],
    )
    is_national_code_verify = models.BooleanField(
        verbose_name='تایید شماره ملی',
        default=False,
    )

    father_name = models.CharField(
        verbose_name='نام پدر',
        max_length=32,
        null=True,
        blank=True,
    )
    is_father_name_verify = models.BooleanField(
        verbose_name='تایید عکس پروفایل',
        default=False,
    )

    mother_name = models.CharField(
        verbose_name='نام مادر',
        max_length=32,
        null=True,
        blank=True,
    )
    is_mother_name_verify = models.BooleanField(
        verbose_name='تایید عکس پروفایل',
        default=False,
    )

    birth_date = models.DateField(
        verbose_name='تاریخ تولد',
        blank=True,
        null=True,
    )
    is_birth_date_verify = models.BooleanField(
        verbose_name='تایید تاریخ تولد',
        default=False,
    )

    birth_place = models.ForeignKey(
        verbose_name='محل تولد',
        to=Zone,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    is_birth_place_verify = models.BooleanField(
        verbose_name='تایید محل تولد',
        default=False,
    )

    nationality = models.ForeignKey(
        verbose_name='ملیت',
        to=BaseInformation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bi_c_nationality',
    )
    is_nationality_verify = models.BooleanField(
        verbose_name='تایید ملیت',
        default=False,
    )
    religion = models.ForeignKey(
        verbose_name='دین',
        to=BaseInformation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bi_c_religion',
    )
    is_religion_verify = models.BooleanField(
        verbose_name='تایید دین',
        default=False,
    )

    official_website = models.URLField(
        verbose_name='وب سایت رسمی',
        null=True,
        blank=True,
        unique=True,
    )
    is_official_website_verify = models.BooleanField(
        verbose_name='تایید وب سایت رسمی',
        default=False,
    )

    def __str__(self):
        return f'{self.username}'

    def to_dict(self):
        return {
            'is_verify': self.is_verify,
            'username': self.username,
            'email': self.email,
            'is_email_verify': self.is_email_verify,
            'phone_number': self.phone_number,
            'is_phone_number_verify': self.is_phone_number_verify,
            'avatar': str(self.avatar),
            'is_avatar_verify': self.is_avatar_verify,
            'first_name': self.first_name,
            'is_first_name_verify': self.is_first_name_verify,
            'last_name': self.last_name,
            'is_last_name_verify': self.is_last_name_verify,
            'gender': self.gender,
            'is_gendre_verify': self.is_gendre_verify,
            'national_code': self.national_code,
            'is_national_code_verify': self.is_national_code_verify,
            'father_name': self.father_name,
            'is_father_name_verify': self.is_father_name_verify,
            'mother_name': self.mother_name,
            'is_mother_name_verify': self.is_mother_name_verify,
            'birth_date': self.birth_date,
            'is_birth_date_verify': self.is_birth_date_verify,
            'birth_place': self.birth_place,
            'is_birth_place_verify': self.is_birth_place_verify,
            'nationality': self.nationality,
            'is_nationality_verify': self.is_nationality_verify,
            'religion': self.religion,
            'is_religion_verify': self.is_religion_verify,
            'official_website': self.official_website,
            'is_official_website_verify': str(self.is_official_website_verify),
            'last_login': self.last_login,
        }

    def save(self, *args, **kwargs):
        if len(self.password) > 21:
            super(User, self).save(*args, **kwargs)
        else:
            from django.contrib.auth.hashers import make_password
            self.password = make_password(self.password)
            super(User, self).save(*args, **kwargs)

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

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

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
