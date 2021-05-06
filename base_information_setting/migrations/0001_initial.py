# Generated by Django 3.2 on 2021-05-06 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('code', models.IntegerField(blank=True, null=True, verbose_name='کد')),
            ],
            options={
                'verbose_name': 'اطلاعات پایه',
                'verbose_name_plural': 'اطلاعات پایه ها',
            },
        ),
        migrations.CreateModel(
            name='BaseInformationHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('title', models.CharField(max_length=64, verbose_name='عنوان')),
                ('code', models.IntegerField(blank=True, null=True, unique=True, verbose_name='کد')),
            ],
            options={
                'verbose_name': 'سرفصل اطلاعات پایه',
                'verbose_name_plural': 'سرفصل های اطلاعات پایه',
            },
        ),
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_email', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='ایمیل')),
                ('_phone_number', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='شماره تلفن')),
                ('_avatar', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='عکس پروفایل')),
                ('_first_name', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='نام')),
                ('_last_name', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='نام خانوادگی')),
                ('_gender', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='جنسیت')),
                ('_national_code', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='کدملی')),
                ('_father_name', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='نام پدر')),
                ('_mother_name', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='نام مادر')),
                ('_birth_date', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='تاریخ تولد')),
                ('_birth_place', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='محل تولد')),
                ('_nationality', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='ملیت')),
                ('_religion', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='دین')),
                ('_official_website', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='وب سایت شخصی')),
                ('_work_expiration', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='سوابق کاری')),
                ('_education_history', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='سوابق کاری')),
                ('_standpoint', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='سوابق کاری')),
                ('_effect', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='سوابق کاری')),
                ('_user_relation', models.CharField(choices=[('0', 'خصوصی'), ('1', 'نمایش عمومی')], default='0', max_length=2, verbose_name='سوابق کاری')),
            ],
            options={
                'verbose_name': 'تنظیمات حریم شخصی',
                'verbose_name_plural': 'تنظیمات حریم\u200cهای شخصی',
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='عنوان منطقه')),
                ('code', models.IntegerField(unique=True, verbose_name='کد')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_information_setting.zone', verbose_name='والد')),
                ('ztype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_information_setting.baseinformation', verbose_name='نوع')),
            ],
            options={
                'verbose_name': 'تقسیمات جغرافیایی',
                'verbose_name_plural': 'تقسیمات جغرافیایی ها',
            },
        ),
        migrations.AddField(
            model_name='baseinformation',
            name='header',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_information_setting.baseinformationheader', verbose_name='سرفصل'),
        ),
        migrations.AddField(
            model_name='baseinformation',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_information_setting.baseinformation', verbose_name='والد'),
        ),
        migrations.AlterUniqueTogether(
            name='baseinformation',
            unique_together={('code', 'header')},
        ),
    ]
