# Generated by Django 3.2 on 2021-05-02 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_candidate_json_t'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='json_t',
        ),
        migrations.CreateModel(
            name='WorkExperition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=128, verbose_name='عنوان جایگاه')),
                ('_cooperation_type', models.CharField(choices=[('0', 'خالی'), ('1', 'پاره وقت'), ('2', 'تمام وقت'), ('3', 'مشاوره')], default='0', max_length=10, verbose_name='نوع همکاری')),
                ('from_date', models.DateField(blank=True, null=True, verbose_name='از تاریخ')),
                ('to_date', models.DateField(blank=True, null=True, verbose_name='تا تاریخ')),
                ('_activity_type', models.CharField(choices=[('0', 'خالی'), ('1', 'قراردادی'), ('2', 'پیمانی'), ('3', 'رسمی')], default='0', max_length=10, verbose_name='نوع فعالیت')),
                ('organization_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='نام سازمان')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'سابقه کاری',
                'verbose_name_plural': 'سوابق کاری',
            },
        ),
    ]
