# Generated by Django 3.2 on 2021-05-04 13:47

from django.db import migrations, models
import repository.regular_expression


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, validators=[repository.regular_expression.UnicodePasswordValidator], verbose_name='کلمه عبور'),
        ),
    ]