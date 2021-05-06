from django.db import models
from users.models import User
from repository.choices import VCODE_CHOICES, VCODE_RETURNER


class BaseInformationHeader(models.Model):
    is_active = models.BooleanField(
        verbose_name='فعال',
        default=False,
    )
    title = models.CharField(
        verbose_name='عنوان',
        max_length=64,
        null=False,
        blank=False,
    )
    code = models.IntegerField(
        verbose_name='کد',
        null=True,
        blank=True,
        unique=True,
    )

    def __str__(self):
        return f'{self.code}: {self.title}' if self.code is not None else f'{self.title}'

    class Meta:
        verbose_name = 'سرفصل اطلاعات پایه'
        verbose_name_plural = 'سرفصل های اطلاعات پایه'

    def to_dict(self):
        return {
            'is_active': self.is_active,
            'title': self.title,
            'code': self.code,
        }


class BaseInformation(models.Model):
    header = models.ForeignKey(
        verbose_name='سرفصل',
        to='BaseInformationHeader',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )
    title = models.CharField(
        verbose_name='عنوان',
        max_length=64,
        null=False,
        blank=False,
    )

    code = models.IntegerField(
        verbose_name='کد',
        null=True,
        blank=True,
    )

    parent = models.ForeignKey(
        verbose_name='والد',
        to='BaseInformation',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.code}: {self.title}' if self.code is not None else f'{self.title}'

    class Meta:
        verbose_name = 'اطلاعات پایه'
        verbose_name_plural = 'اطلاعات پایه ها'
        unique_together = ('code', 'header',)

    def to_dict(self):
        return {
            'header': self.header.to_dict(),
            'title': self.title,
            'code': self.code,
            'parent': self.parent.to_dict(),
        }


class Zone(models.Model):
    title = models.CharField(
        verbose_name='عنوان منطقه',
        max_length=32,
        blank=False,
        null=False,
    )
    code = models.IntegerField(
        verbose_name='کد',
        unique=True,
        blank=False,
        null=False,
    )
    ztype = models.ForeignKey(
        verbose_name='نوع',
        to='BaseInformation',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    parent = models.ForeignKey(
        verbose_name='والد',
        to='Zone',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'تقسیمات جغرافیایی'
        verbose_name_plural = 'تقسیمات جغرافیایی ها'

    def __str__(self):
        return f'{self.ztype} {self.title}'

    def to_dict(self):
        return {
            'title': self.title,
            'code': self.code,
            'type': self.ztype,
            'parent': self.parent,
        }


class VCode(models.Model):
    user = models.ForeignKey(
        verbose_name='کاربر',
        to=User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
    )
    string = models.CharField(
        verbose_name='کد',
        max_length=5,
        null=False,
        blank=False,
        editable=False
    )
    _vctype = models.CharField(
        verbose_name='نوع',
        max_length=2,
        null=False,
        blank=False,
        choices=VCODE_CHOICES,
    )

    @property
    def vctype(self):
        return VCODE_RETURNER(self._vctype)

    @vctype.setter
    def vctype(self, value):
        self._vctype = value

    expiration_date = models.DateTimeField(
        verbose_name='تاریخ انقضا',
        null=False,
        blank=False,
        editable=False,
    )
    used = models.BooleanField(
        verbose_name='استفاده شده',
        default=False,
    )
    valid = models.BooleanField(
        verbose_name='قابل قبول',
        default=False,
    )

    @property
    def expired(self):
        from django.utils import timezone
        now = timezone.now()
        return self.expiration_date < now

    def __str__(self):
        return 'Expiration date: {}'.format(self.expiration_date)


def create_vcode(user: User = None, vtype: str = None):
    if user is None or vtype is None:
        return None
    last_vcodes = VCode.objects. \
        filter(user=user). \
        filter(vtype=vtype). \
        filter(used=False). \
        filter(valid=True).all()

    for last_vcode in last_vcodes:
        last_vcode.valid = False
        last_vcode.save()

    from django.utils import timezone
    import random
    vc = VCode()
    vc.user = user

    vcode = random.randint(10000, 99999)
    vc.string = str(vcode)

    vc.vctype = vtype

    now = timezone.now()
    delta = timezone.timedelta(minutes=10)
    vc.expiration_date = now + delta

    vc.valid = True
    vc.save()
    return vc.string


def vcode_is_acceptable(code: str = None, user: User = None, vtype: str = None) -> bool:
    if code is None or user is None or vtype is None:
        return False
    vcode = VCode.objects. \
        filter(string=code). \
        filter(user=user). \
        filter(vtype=vtype). \
        filter(used=False). \
        filter(valid=True).first()
    if vcode is None:
        return False
    if vcode.expired:
        return False
    vcode.used = True
    vcode.save()
    return True
