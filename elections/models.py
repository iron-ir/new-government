from django.db import models
from base_information_settings.models import BaseInformation, BaseInformationHeader, Zone
from users.models import User


class Election(models.Model):
    etype = models.ForeignKey(
        verbose_name='نوع',
        to=BaseInformation,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    form_year = models.IntegerField(
        verbose_name='از سال',
        null=False,
        blank=False,
    )
    to_year = models.IntegerField(
        verbose_name='تا سال',
        null=False,
        blank=False,
    )
    period = models.IntegerField(
        verbose_name='دوره',
        null=False,
        blank=False,
    )

    date = models.DateField(
        verbose_name='تاریخ برگزاری',
        null=False,
        blank=False
    )
    duration_of_the_event = models.DateField(
        verbose_name='مدت زمان برگزاری',
        null=True,
        blank=True,
    )
    round = models.IntegerField(
        verbose_name='دور',
        default=1,
    )

    class Meta:
        verbose_name = 'انتخابات'
        verbose_name_plural = 'انتخابات ها'

    def __str__(self):
        return f'{self.period} {self.etype}'

    def to_dict(self):
        return {
            'type': self.etype.to_dict(),
            'form_year': self.form_year,
            'to_year': self.to_year,
            'period': self.period,
            'date': self.date,
            'duration_of_the_event': self.duration_of_the_event,
            'round': self.round,
        }


class RegisterCandidatePerElection(models.Model):
    candidate = models.ForeignKey(
        verbose_name='نامزد',
        to='Candidate',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    election = models.ForeignKey(
        verbose_name='انتخابات',
        to=Election,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    candidate_group = models.ForeignKey(
        verbose_name='ائتلاف',
        to='CandidateGroup',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    date_time = models.DateTimeField(
        verbose_name='تاریخ ثبت نام',
        null=False,
        blank=False,
    )
    slogan = models.CharField(
        verbose_name='شعار',
        max_length=256,
        null=True,
        blank=True,
    )
    candidate_title = models.CharField(
        verbose_name='عنوان نامزد',
        max_length=128,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'نماینده شرکت کننده در انتخابات'
        verbose_name_plural = 'نمایندگان شرکت کننده در انتخابات ها'

    def __str__(self):
        return f'{self.candidate}, {self.election}'

    def to_dict(self):
        return {
            'user': self.candidate.to_dict(),
            'elections': self.election.to_dict(),
            'candidate_group': self.candidate_group.to_dict(),
            'date_time': self.date_time,
            'slogan': self.slogan,
            'candidate_title': self.candidate_title,
        }


class Candidate(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
        null=False,
        blank=False,
    )
    _is_suspension = models.BooleanField(
        verbose_name='تعلیق',
        default=False,
    )

    @property
    def is_suspension(self):
        if self.user.is_personal_information_verify:
            self._is_suspension = False
        else:
            self._is_suspension = True
        return self._is_suspension

    def __str__(self):
        return f'{self.user}'

    def to_dict(self):
        return {
            'user': self.user.to_dict(),
            'is_suspension': self.is_suspension,
        }

    class Meta:
        verbose_name = 'کاندید'
        verbose_name_plural = 'کاندیدها'


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

    def to_dict(self):
        return {
            'title': self.title,
        }
