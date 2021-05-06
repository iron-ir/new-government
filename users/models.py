from django.db import models
from django.contrib.auth.models import AbstractUser
from repository.uploader import image_upload_to, file_upload_to
from repository.regular_expression import UnicodeNationalcodeValidator, UnicodePhoneNumberValidator
from repository.choices import *
from base_information_settings.models import BaseInformation, BaseInformationHeader, Zone


class Privacy(models.Model):
    _email = models.CharField(
        max_length=2,
        verbose_name='ایمیل',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def email(self):
        return PRIVACY_RETURNER(self._email)

    @email.setter
    def email(self, value):
        self._email = value

    _phone_number = models.CharField(
        max_length=2,
        verbose_name='شماره تلفن',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def phone_number(self):
        return PRIVACY_RETURNER(self._phone_number)

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    _avatar = models.CharField(
        max_length=2,
        verbose_name='عکس پروفایل',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def avatar(self):
        return PRIVACY_RETURNER(self._avatar)

    @avatar.setter
    def avatar(self, value):
        self._avatar = value

    _first_name = models.CharField(
        max_length=2,
        verbose_name='نام',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def first_name(self):
        return PRIVACY_RETURNER(self._first_name)

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    _last_name = models.CharField(
        max_length=2,
        verbose_name='نام خانوادگی',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def last_name(self):
        return PRIVACY_RETURNER(self._last_name)

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    _gender = models.CharField(
        max_length=2,
        verbose_name='جنسیت',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def gender(self):
        return PRIVACY_RETURNER(self._gender)

    @gender.setter
    def gender(self, value):
        self._gender = value

    _national_code = models.CharField(
        max_length=2,
        verbose_name='کدملی',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def national_code(self):
        return PRIVACY_RETURNER(self._national_code)

    @national_code.setter
    def national_code(self, value):
        self._national_code = value

    _father_name = models.CharField(
        max_length=2,
        verbose_name='نام پدر',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def father_name(self):
        return PRIVACY_RETURNER(self._father_name)

    @father_name.setter
    def father_name(self, value):
        self._father_name = value

    _mother_name = models.CharField(
        max_length=2,
        verbose_name='نام مادر',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def mother_name(self):
        return PRIVACY_RETURNER(self._mother_name)

    @mother_name.setter
    def mother_name(self, value):
        self._mother_name = value

    _birth_date = models.CharField(
        max_length=2,
        verbose_name='تاریخ تولد',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def birth_date(self):
        return PRIVACY_RETURNER(self._birth_date)

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    _birth_place = models.CharField(
        max_length=2,
        verbose_name='محل تولد',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def birth_place(self):
        return PRIVACY_RETURNER(self._birth_place)

    @birth_place.setter
    def birth_place(self, value):
        self._birth_place = value

    _nationality = models.CharField(
        max_length=2,
        verbose_name='ملیت',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def nationality(self):
        return PRIVACY_RETURNER(self._nationality)

    @nationality.setter
    def nationality(self, value):
        self._nationality = value

    _religion = models.CharField(
        max_length=2,
        verbose_name='دین',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def religion(self):
        return PRIVACY_RETURNER(self._religion)

    @religion.setter
    def religion(self, value):
        self._religion = value

    _official_website = models.CharField(
        max_length=2,
        verbose_name='وب سایت شخصی',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def official_website(self):
        return PRIVACY_RETURNER(self._official_website)

    @official_website.setter
    def official_website(self, value):
        self._official_website = value

    _work_expiration = models.CharField(
        max_length=2,
        verbose_name='سوابق کاری',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def work_expiration(self):
        return PRIVACY_RETURNER(self._work_expiration)

    @work_expiration.setter
    def work_expiration(self, value):
        self._work_expiration = value

    _education_history = models.CharField(
        max_length=2,
        verbose_name='سوابق کاری',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def education_history(self):
        return PRIVACY_RETURNER(self._education_history)

    @education_history.setter
    def education_history(self, value):
        self._education_history = value

    _standpoint = models.CharField(
        max_length=2,
        verbose_name='سوابق کاری',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def standpoint(self):
        return PRIVACY_RETURNER(self._standpoint)

    @standpoint.setter
    def standpoint(self, value):
        self._standpoint = value

    _effect = models.CharField(
        max_length=2,
        verbose_name='سوابق کاری',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def effect(self):
        return PRIVACY_RETURNER(self._effect)

    @effect.setter
    def effect(self, value):
        self._effect = value

    _user_relation = models.CharField(
        max_length=2,
        verbose_name='سوابق کاری',
        default=PRIVACY_DEFAULT,
        choices=PRIVACY_CHOICES,
    )

    @property
    def user_relation(self):
        return PRIVACY_RETURNER(self._user_relation)

    @user_relation.setter
    def user_relation(self, value):
        self._user_relation = value

    def to_dict(self):
        return {
            'email': self.email,
            'phone_number': self.phone_number,
            'avatar': self.avatar,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'national_code': self.national_code,
            'father_name': self.father_name,
            'mother_name': self.mother_name,
            'birth_date': self.birth_date,
            'birth_place': self.birth_place,
            'nationality': self.nationality,
            'religion': self.religion,
            'official_website': self.official_website,
            'work_expiration': self.work_expiration,
            'education_history': self.education_history,
            'standpoint': self.standpoint,
            'effect': self.effect,
            'user_relation': self.user_relation,

        }

    class Meta:
        verbose_name = 'تنظیمات حریم شخصی'
        verbose_name_plural = 'تنظیمات حریم‌های شخصی'


class User(AbstractUser):
    privacy = models.OneToOneField(
        to=Privacy,
        on_delete=models.CASCADE,
        verbose_name='حریم شخصی',
        null=True,
        blank=True,
    )
    _is_verify = models.BooleanField(
        verbose_name='تایید',
        default=False,
    )

    @property
    def is_verify(self):
        self._is_verify = self.is_email_verify and \
                          self.is_phone_number_verify and \
                          self.is_personal_information_verify
        return self._is_verify

    is_personal_information_verify = models.BooleanField(
        verbose_name='تایید اطلاعات شخصی',
        default=False,
    )

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
    first_name = models.CharField(
        verbose_name='نام',
        max_length=64,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        verbose_name='نام خانوادگی',
        max_length=64,
        null=True,
        blank=True,
    )
    _gender = models.CharField(
        verbose_name='جنسیت',
        max_length=1,
        default=GENDER_DEFAULT,
        choices=GENDER_CHOICES,
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

    father_name = models.CharField(
        verbose_name='نام پدر',
        max_length=32,
        null=True,
        blank=True,
    )

    mother_name = models.CharField(
        verbose_name='نام مادر',
        max_length=32,
        null=True,
        blank=True,
    )

    birth_date = models.DateField(
        verbose_name='تاریخ تولد',
        blank=True,
        null=True,
    )

    birth_place = models.ForeignKey(
        verbose_name='محل تولد',
        to=Zone,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    nationality = models.ForeignKey(
        verbose_name='ملیت',
        to=BaseInformation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bi_c_nationality',
    )
    religion = models.ForeignKey(
        verbose_name='دین',
        to=BaseInformation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='bi_c_religion',
    )

    official_website = models.URLField(
        verbose_name='وب سایت رسمی',
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return f'{self.username}'

    def to_dict(self):
        return {
            'is_verify': self.is_verify,
            'is_email_verify': self.is_email_verify,
            'is_phone_number_verify': self.is_phone_number_verify,
            'is_personal_information_verify': self.is_personal_information_verify,
            'username': self.username,
            'email': self.email,
            'phone_number': self.phone_number,
            'avatar': str(self.avatar),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'gender': self.gender,
            'national_code': self.national_code,
            'father_name': self.father_name,
            'mother_name': self.mother_name,
            'birth_date': self.birth_date,
            'birth_place': self.birth_place,
            'nationality': self.nationality,
            'religion': self.religion,
            'official_website': str(self.official_website),
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


class WorkExpiration(models.Model):
    is_verify = models.BooleanField(
        verbose_name='تایید',
        default=False,
    )
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

    def to_dict(self):
        return {
            'is_verify': self.is_verify,
            'user': self.user.to_dict(),
            'post_title': self.post_title,
            'cooperation_type': self.cooperation_type.to_dict(),
            'from_date': self.from_date,
            'to_date': self.to_date,
            'activity_type': self.activity_type.to_dict(),
            'organization_name': self.organization_name,
        }


class EducationHistory(models.Model):
    is_verify = models.BooleanField(
        verbose_name='تایید',
        default=False,
    )
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

    def to_dict(self):
        return {
            'is_verify': self.is_verify,
            'user': self.user.to_dict(),
            'degree_type': self.degree_type.to_dict(),
            'field_of_study': self.field_of_study.to_dict(),
            'place_of_study_type': self.place_of_study_type.to_dict(),
            'place_of_study': self.place_of_study,
            'zone': self.zone.to_dict(),
            'graduation_date': self.graduation_date,
            'is_study': self.is_study,
        }


class Standpoint(models.Model):
    user = models.ForeignKey(
        verbose_name='نامزد',
        to=User,
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
        return f'{self.user}: {self.title}'

    def to_dict(self):
        return {
            'user': self.user.to_dict(),
            'title': self.title,
            'description': self.description,
            'is_active': self.is_active,
            'link': self.link,
            'attachment': self.attachment,
        }


class Effect(models.Model):
    is_active = models.BooleanField(
        verbose_name='فعال',
        default=False,
    )
    user = models.ForeignKey(
        verbose_name='کاربر',
        to=User,
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
        return f'{self.user}: {self.title}'

    def to_dict(self):
        return {
            'is_active': self.is_active,
            'user': self.user.to_dict(),
            'title': self.title,
            'description': self.description,
            'link': self.link,
            'attachment': self.attachment,
        }


class UserRelation(models.Model):
    a_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='نامزد',
        null=False,
        blank=False,
        related_name='u_ur_a_user',
    )
    b_user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
        null=False,
        blank=False,
        related_name='u_ur_b_user',
    )
    rtype = models.ForeignKey(
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
        return f'{self.a_user}, {self.b_user}'

    def to_dict(self):
        return {
            'a_user': self.a_user.to_dict(),
            'b_user': self.b_user.to_dict(),
            'type': self.rtype.to_dict(),
            'form_date': self.form_date,
            'to_date': self.to_date,
        }
