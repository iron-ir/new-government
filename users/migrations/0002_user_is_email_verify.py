# Generated by Django 3.2 on 2021-05-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_email_verify',
            field=models.BooleanField(default=False, verbose_name='تایید ایمیل'),
        ),
    ]
