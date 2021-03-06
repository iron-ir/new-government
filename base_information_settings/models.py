from django.db import models


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
            'id': self.pk,
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
        return f'{self.code}:{self.header.title}-{self.title}' if self.code is not None else f'{self.header.title}-{self.title}'

    class Meta:
        verbose_name = 'اطلاعات پایه'
        verbose_name_plural = 'اطلاعات پایه ها'
        unique_together = ('code', 'header',)

    def to_dict(self):
        return {
            'id': self.pk,
            'header': self.header_id,
            'title': self.title,
            'code': self.code,
            'parent': self.parent_id,
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
            'id': self.pk,
            'title': self.title,
            'code': self.code,
            'type': self.ztype,
            'parent': self.parent,
        }


class Role(models.Model):
    title = models.ForeignKey(
        to=BaseInformation,
        on_delete=models.CASCADE,
        verbose_name='عنوان',
        blank=False,
        null=False,
    )
    is_active = models.BooleanField(
        verbose_name='فعال',
        default=False,
    )

    class Meta:
        verbose_name = 'نقش'
        verbose_name_plural = 'نقش ها'

    def __str__(self):
        return f'{self.title}'

    def to_dict(self):
        return {
            'id': self.pk,
            'title': self.title,
            'is_active': self.is_active,
        }
