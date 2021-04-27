# Generated by Django 3.2 on 2021-04-27 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userrole',
            name='role',
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='user',
        ),
        migrations.RemoveField(
            model_name='vcode',
            name='user',
        ),
        migrations.RemoveField(
            model_name='workexperition',
            name='user',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='_verified_nationalcode',
            new_name='_is_national_code',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='_verified_phonenumber',
            new_name='_is_phone_number_verify',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='_verified',
            new_name='_verified_badge',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='birthday',
            new_name='birth_date',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='nationalcode',
            new_name='national_code',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phonenumber',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='_gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='_is_candidate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='city_of_residence',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='UserRole',
        ),
        migrations.DeleteModel(
            name='VCode',
        ),
        migrations.DeleteModel(
            name='WorkExperition',
        ),
    ]
