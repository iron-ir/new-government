# Generated by Django 3.2 on 2021-04-25 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_candidate',
            field=models.BooleanField(default=False, verbose_name='نامزد انتخاباتی'),
        ),
    ]
